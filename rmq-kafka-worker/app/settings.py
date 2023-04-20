import os

RMQ_HOST = os.environ.get("RMQ_HOST")
RMQ_USER = os.environ.get("RMQ_USER")
RMQ_PASS = os.environ.get("RMQ_PASS")
RMQ_PORT = os.environ.get("RMQ_PORT")
RMQ_CONNSTR = f"amqp://{RMQ_USER}:{RMQ_PASS}@{RMQ_HOST}:{RMQ_PORT}"

KAFKA_HOST = os.environ.get("KAFKA_HOST")
KAFKA_PORT = os.environ.get("KAFKA_PORT")
