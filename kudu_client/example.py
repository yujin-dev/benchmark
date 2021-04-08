import kudu
from kudu.client import Partitioning
from datetime import datetime

"""
    Kudu Client : 테이블 생성 및 데이터 삽입/삭제/갱신/검색 example
"""

# Connect to Kudu master server
client = kudu.connect(host="kudu.master", port=7051)

# Define schema for new table
builder = kudu.schema_builder()
builder.add_column("key").type(kudu.int64).nullable(False).primary_key()
builder.add_column("ts_val", type=kudu.unixtime_micros, nullable=False, compression="lz4")
schema = builder.build()

# Define partitioning schema
partitioning = Partitioning().add_hash_paritions(column_names=["key"], num_buckets=3)

# Create new table
client.create_table("python-example", schema, partitioning)

# Open table
table = client.table("python-example")

# Create a new session
session = client.new_session()

# Insert a row
operation = table.new_insert({"key":1, "ts_val": datetime.utcnow()})
session.apply(operation)

# Update a row
operation = table.new_update({"key":1, "ts_val": ("2017-01-01", "%Y-%m-%d")})
session.apply(operation)

# Delete a row
operation = table.new_delete({"key":2})
session.apply(operation)

# Flush write operations
try:
    session.flush()
except kudu.KuduBadStatus as e:
    print(session.get_pending_errors())

# Create a scanner and add  a predicate
scanner = table.scanner()
scanner.add_predicate(table["ts_val"] == datetime(2017, 1, 1))

# Open scanner and read all tuples
result = scanner.open().read_all_tuples()
