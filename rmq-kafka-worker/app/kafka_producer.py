import json
import avro.schema
import avro.io
from kafka import KafkaProducer


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=["kafka:9092"],
    value_serializer=json_serializer
)


def send(message):
    producer.send("vehicle", value=message)
    print("message sent to Kafka")
