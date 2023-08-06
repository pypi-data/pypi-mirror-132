#ifndef STREAM_DATAFRAME_STREAM_VINEYARD_H
#define STREAM_DATAFRAME_STREAM_VINEYARD_H

/** Copyright 2020-2021 Alibaba Group Holding Limited.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

#ifndef MODULES_BASIC_STREAM_DATAFRAME_STREAM_MOD_H_
#define MODULES_BASIC_STREAM_DATAFRAME_STREAM_MOD_H_

#include <memory>
#include <string>
#include <utility>
#include <vector>

#include "arrow/util/config.h"
#include "arrow/util/key_value_metadata.h"

#include "basic/ds/dataframe.vineyard.h"
#include "basic/stream/stream_utils.h"
#include "client/client.h"
#include "client/ds/blob.h"
#include "client/ds/i_object.h"
#include "common/util/uuid.h"

namespace vineyard {

#ifdef __GNUC__
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wattributes"
#endif

class Client;

class __attribute__((annotate("no-vineyard"))) DataframeStreamWriter {
 public:
  const size_t MaximumChunkSize() const { return -1; }

  Status GetNext(size_t const size,
                 std::unique_ptr<arrow::MutableBuffer>& buffer) {
    return client_.GetNextStreamChunk(id_, size, buffer);
  }

  Status Abort() {
    if (stoped_) {
      return Status::OK();
    }
    stoped_ = true;
    return client_.StopStream(id_, true);
  }

  Status Finish() {
    if (stoped_) {
      return Status::OK();
    }
    stoped_ = true;
    return client_.StopStream(id_, false);
  }

  Status WriteTable(std::shared_ptr<arrow::Table> table) {
    std::vector<std::shared_ptr<arrow::RecordBatch>> batches;
    RETURN_ON_ERROR(TableToRecordBatches(table, &batches));
    for (auto const& batch : batches) {
      RETURN_ON_ERROR(WriteBatch(batch));
    }
    return Status::OK();
  }

  Status WriteBatch(std::shared_ptr<arrow::RecordBatch> batch) {
    size_t size = 0;
    RETURN_ON_ERROR(GetRecordBatchStreamSize(*batch, &size));
    std::unique_ptr<arrow::MutableBuffer> buffer;
    RETURN_ON_ERROR(GetNext(size, buffer));
    arrow::io::FixedSizeBufferWriter stream(std::move(buffer));

    std::shared_ptr<arrow::ipc::RecordBatchWriter> writer;
#if defined(ARROW_VERSION) && ARROW_VERSION < 17000
    RETURN_ON_ARROW_ERROR(arrow::ipc::RecordBatchStreamWriter::Open(
        &stream, batch->schema(), &writer));
#elif defined(ARROW_VERSION) && ARROW_VERSION < 2000000
    RETURN_ON_ARROW_ERROR_AND_ASSIGN(
        writer, arrow::ipc::NewStreamWriter(&stream, batch->schema()));
#else
    RETURN_ON_ARROW_ERROR_AND_ASSIGN(
        writer, arrow::ipc::MakeStreamWriter(&stream, batch->schema()));
#endif
    RETURN_ON_ARROW_ERROR(writer->WriteRecordBatch(*batch));
    RETURN_ON_ARROW_ERROR(writer->Close());
    return Status::OK();
  }

  Status WriteDataframe(std::shared_ptr<DataFrame> df) {
    return WriteBatch(df->AsBatch());
  }

  DataframeStreamWriter(Client& client, ObjectID const& id,
                        ObjectMeta const& meta)
      : client_(client), id_(id), meta_(meta), stoped_(false) {}

 private:
  Client& client_;
  ObjectID id_;
  ObjectMeta meta_;
  bool stoped_;  // an optimization: avoid repeated idempotent requests.

  friend class Client;
};

class __attribute__((annotate("no-vineyard"))) DataframeStreamReader {
 public:
  Status GetNext(std::unique_ptr<arrow::Buffer>& buffer) {
    return client_.PullNextStreamChunk(id_, buffer);
  }

  Status ReadRecordBatches(
      std::vector<std::shared_ptr<arrow::RecordBatch>>& batches) {
    std::shared_ptr<arrow::RecordBatch> batch;
    std::unique_ptr<arrow::Buffer> buf;

    while (GetNext(buf).ok()) {
      std::shared_ptr<arrow::Buffer> copied_buffer;
#if defined(ARROW_VERSION) && ARROW_VERSION < 17000
      RETURN_ON_ARROW_ERROR(buf->Copy(0, buf->size(), &copied_buffer));
#else
      RETURN_ON_ARROW_ERROR_AND_ASSIGN(copied_buffer,
                                       buf->CopySlice(0, buf->size()));
#endif
      auto buffer_reader =
          std::make_shared<arrow::io::BufferReader>(copied_buffer);
      std::shared_ptr<arrow::ipc::RecordBatchReader> reader;
#if defined(ARROW_VERSION) && ARROW_VERSION < 17000
      RETURN_ON_ARROW_ERROR(
          arrow::ipc::RecordBatchStreamReader::Open(buffer_reader, &reader));
#else
      RETURN_ON_ARROW_ERROR_AND_ASSIGN(
          reader, arrow::ipc::RecordBatchStreamReader::Open(buffer_reader));
#endif
      RETURN_ON_ARROW_ERROR(reader->ReadNext(&batch));

      std::shared_ptr<arrow::KeyValueMetadata> metadata;
      if (batch->schema()->metadata() != nullptr) {
        metadata = batch->schema()->metadata()->Copy();
      } else {
        metadata.reset(new arrow::KeyValueMetadata());
      }

#if defined(ARROW_VERSION) && ARROW_VERSION < 17000
      std::unordered_map<std::string, std::string> metakv;
      metadata->ToUnorderedMap(&metakv);
      for (auto const& kv : params_) {
        metakv[kv.first] = kv.second;
      }
      metadata = std::make_shared<arrow::KeyValueMetadata>();
      for (auto const& kv : metakv) {
        metadata->Append(kv.first, kv.second);
      }
#else
      for (auto const& kv : params_) {
        CHECK_ARROW_ERROR(metadata->Set(kv.first, kv.second));
      }
#endif

      batches.push_back(batch->ReplaceSchemaMetadata(metadata));
    }
    return Status::OK();
  }

  Status ReadTable(std::shared_ptr<arrow::Table>& table) {
    std::vector<std::shared_ptr<arrow::RecordBatch>> batches;
    RETURN_ON_ERROR(this->ReadRecordBatches(batches));
#if defined(ARROW_VERSION) && ARROW_VERSION < 17000
    RETURN_ON_ARROW_ERROR(arrow::Table::FromRecordBatches(batches, &table));
#else
    RETURN_ON_ARROW_ERROR_AND_ASSIGN(table,
                                     arrow::Table::FromRecordBatches(batches));
#endif
    return Status::OK();
  }

  Status ReadBatch(std::shared_ptr<arrow::RecordBatch>& batch) {
    std::unique_ptr<arrow::Buffer> buf;

    auto status = GetNext(buf);
    if (status.ok()) {
      std::shared_ptr<arrow::Buffer> copied_buffer;
#if defined(ARROW_VERSION) && ARROW_VERSION < 17000
      RETURN_ON_ARROW_ERROR(buf->Copy(0, buf->size(), &copied_buffer));
#else
      RETURN_ON_ARROW_ERROR_AND_ASSIGN(copied_buffer,
                                       buf->CopySlice(0, buf->size()));
#endif
      auto buffer_reader =
          std::make_shared<arrow::io::BufferReader>(copied_buffer);
      std::shared_ptr<arrow::ipc::RecordBatchReader> reader;
#if defined(ARROW_VERSION) && ARROW_VERSION < 17000
      RETURN_ON_ARROW_ERROR(
          arrow::ipc::RecordBatchStreamReader::Open(buffer_reader, &reader));
#else
      RETURN_ON_ARROW_ERROR_AND_ASSIGN(
          reader, arrow::ipc::RecordBatchStreamReader::Open(buffer_reader));
#endif
      RETURN_ON_ARROW_ERROR(reader->ReadNext(&batch));

      std::shared_ptr<arrow::KeyValueMetadata> metadata;
      if (batch->schema()->metadata() != nullptr) {
        metadata = batch->schema()->metadata()->Copy();
      } else {
        metadata.reset(new arrow::KeyValueMetadata());
      }

#if defined(ARROW_VERSION) && ARROW_VERSION < 17000
      std::unordered_map<std::string, std::string> metakv;
      metadata->ToUnorderedMap(&metakv);
      for (auto const& kv : params_) {
        metakv[kv.first] = kv.second;
      }
      metadata = std::make_shared<arrow::KeyValueMetadata>();
      for (auto const& kv : metakv) {
        metadata->Append(kv.first, kv.second);
      }
#else
      for (auto const& kv : params_) {
        CHECK_ARROW_ERROR(metadata->Set(kv.first, kv.second));
      }
#endif

      batch = batch->ReplaceSchemaMetadata(metadata);
    }
    return status;
  }

  Status ReadLine(std::string& line) {
    if (!batch_ || cursor_ == batch_->num_rows()) {
      cursor_ = 0;
      std::unique_ptr<arrow::Buffer> buf;
      if (!GetNext(buf).ok())
        return Status::EndOfFile();
      auto buffer_reader =
          std::make_shared<arrow::io::BufferReader>(std::move(buf));
      std::shared_ptr<arrow::ipc::RecordBatchReader> reader;
#if defined(ARROW_VERSION) && ARROW_VERSION < 17000
      RETURN_ON_ARROW_ERROR(
          arrow::ipc::RecordBatchStreamReader::Open(buffer_reader, &reader));
#else
      RETURN_ON_ARROW_ERROR_AND_ASSIGN(
          reader, arrow::ipc::RecordBatchStreamReader::Open(buffer_reader));
#endif
      RETURN_ON_ARROW_ERROR(reader->ReadNext(&batch_));
    }
    auto s = batch_->Slice(cursor_, 1);
    std::ostringstream ss;
    for (int i = 0; i < s->num_columns(); ++i) {
      auto c = std::dynamic_pointer_cast<arrow::Int64Array>(s->column(i));
      if (c) {
        ss << c->GetView(0);
      }
      if (i < s->num_columns() - 1) {
        if (params_.find("delimiter") == params_.end()) {
          ss << ",";
        } else {
          ss << params_["delimiter"];
        }
      } else {
        ss << "\n";
      }
    }
    line = ss.str();
    cursor_++;
    return Status::OK();
  }

  Status GetHeaderLine(bool& header_row, std::string& header_line) {
    if (params_.find("header_row") != params_.end()) {
      header_row = (params_["header_row"] == "1");
      if (params_.find("header_line") != params_.end()) {
        header_line = params_["header_line"];
      } else {
        header_line = "";
      }
    } else {
      header_row = false;
      header_line = "";
    }
    return Status::OK();
  }

  DataframeStreamReader(
      Client& client, ObjectID const& id, ObjectMeta const& meta,
      std::unordered_map<std::string, std::string> const& params)
      : client_(client),
        id_(id),
        meta_(meta),
        params_(params),
        batch_(nullptr),
        cursor_(0){};

 private:
  Client& client_;
  ObjectID id_;
  ObjectMeta meta_;
  std::unordered_map<std::string, std::string> params_;
  std::vector<std::shared_ptr<arrow::RecordBatch>> batches_;
  std::shared_ptr<arrow::RecordBatch> batch_;
  int64_t cursor_;

  friend class Client;
};

class DataframeStream : public Registered<DataframeStream> {
 
  public:
    static std::unique_ptr<Object> Create() __attribute__((used)) {
        return std::static_pointer_cast<Object>(
            std::unique_ptr<DataframeStream>{
                new DataframeStream()});
    }


  public:
    void Construct(const ObjectMeta& meta) override {
        std::string __type_name = type_name<DataframeStream>();
        VINEYARD_ASSERT(
            meta.GetTypeName() == __type_name,
            "Expect typename '" + __type_name + "', but got '" + meta.GetTypeName() + "'");
        this->meta_ = meta;
        this->id_ = meta.GetId();

        meta.GetKeyValue("params_", this->params_);

        
    }

 private:
public:
  Status OpenReader(Client& client,
                    std::unique_ptr<DataframeStreamReader>& reader) {
    RETURN_ON_ERROR(client.OpenStream(id_, OpenStreamMode::read));
    reader = std::unique_ptr<DataframeStreamReader>(
        new DataframeStreamReader(client, id_, meta_, params_));
    return Status::OK();
  }

  Status OpenWriter(Client& client,
                    std::unique_ptr<DataframeStreamWriter>& writer) {
    RETURN_ON_ERROR(client.OpenStream(id_, OpenStreamMode::write));
    writer = std::unique_ptr<DataframeStreamWriter>(
        new DataframeStreamWriter(client, id_, meta_));
    return Status::OK();
  }

  std::unordered_map<std::string, std::string> GetParams() { return params_; }

 private:
  __attribute__((annotate("codegen")))
  std::unordered_map<std::string, std::string>
      params_;

  friend class Client;
  friend class DataframeStreamBaseBuilder;
};

#ifdef __GNUC__
#pragma GCC diagnostic pop
#endif

}  // namespace vineyard

#endif  // MODULES_BASIC_STREAM_DATAFRAME_STREAM_MOD_H_

namespace vineyard {


class DataframeStreamBaseBuilder: public ObjectBuilder {
  public:
    

    explicit DataframeStreamBaseBuilder(Client &client) {}

    explicit DataframeStreamBaseBuilder(
            DataframeStream const &__value) {
        this->set_params_(__value.params_);
    }

    explicit DataframeStreamBaseBuilder(
            std::shared_ptr<DataframeStream> const & __value):
        DataframeStreamBaseBuilder(*__value) {
    }

    std::shared_ptr<Object> _Seal(Client &client) override {
        // ensure the builder hasn't been sealed yet.
        ENSURE_NOT_SEALED(this);

        VINEYARD_CHECK_OK(this->Build(client));
        auto __value = std::make_shared<DataframeStream>();

        size_t __value_nbytes = 0;

        __value->meta_.SetTypeName(type_name<DataframeStream>());
        if (std::is_base_of<GlobalObject, DataframeStream>::value) {
            __value->meta_.SetGlobal(true);
        }

        __value->params_ = params_;
        __value->meta_.AddKeyValue("params_", __value->params_);

        __value->meta_.SetNBytes(__value_nbytes);

        VINEYARD_CHECK_OK(client.CreateMetaData(__value->meta_, __value->id_));

        // mark the builder as sealed
        this->set_sealed(true);

        
        return std::static_pointer_cast<Object>(__value);
    }

    Status Build(Client &client) override {
        return Status::OK();
    }

  protected:
    std::unordered_map<std::string, std::string> params_;

    void set_params_(std::unordered_map<std::string, std::string> const &params__) {
        this->params_ = params__;
    }
};


}  // namespace vineyard


#endif // STREAM_DATAFRAME_STREAM_VINEYARD_H
