import json
import avro.schema
import avro.io
from kafka import KafkaProducer

import settings


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=[f"{settings.KAFKA_HOST}:{settings.KAFKA_PORT}"],
    value_serializer=json_serializer
)


def send(message):
    producer.send("vehicle", value=message)
    print("message sent to Kafka")
