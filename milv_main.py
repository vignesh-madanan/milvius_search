from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)
import random

_HOST = "localhost"
_PORT = "19530"


class MilviusManager:
    def __init__(self):
        self.hello_milvus = None
        self.create_connection()

    def create_connection(self):
        print("\nCreate connection...")
        connections.connect(host=_HOST, port=_PORT)
        print("\nList connections:")
        print(connections.list_connections())

    def create_schema(self):
        fields = [
            FieldSchema(
                name="pk", dtype=DataType.INT64, is_primary=True, auto_id=False
            ),
            FieldSchema(name="random", dtype=DataType.DOUBLE),
            FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=8),
        ]
        schema = CollectionSchema(
            fields, "hello_milvus is the simplest demo to introduce the APIs"
        )
        self.hello_milvus = Collection("hello_milvus", schema)

    def insert_data(self):
        entities = [
            [i for i in range(3000)],  # field pk
            [float(random.randrange(-20, -10)) for _ in range(3000)],  # field random
            [
                [random.random() for _ in range(8)] for _ in range(3000)
            ],  # field embeddings
        ]
        insert_result = self.hello_milvus.insert(entities)
        return insert_result


def main():
    mm = MilviusManager()
    mm.create_schema()
    mm.insert_data()


if __name__ == "__main__":
    main()
