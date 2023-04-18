import logging
import socket

from kombu import Connection, Exchange, Queue, Consumer

import settings
import kafka_producer

log = logging.getLogger(__name__)


class RMQConsumer:
    """Consumes RabbitMQ messages"""

    def __init__(self):
        self.exchange = Exchange("vehicle", type="topic", durable=True)
        self.queue = Queue(name="vehicle", exchange=self.exchange, routing_key="vehicle.*.*")
        self.conn = Connection(settings.RMQ_CONNSTR, heartbeat=10)
        self.consumer = Consumer(self.conn, queues=self.queue, callbacks=[self.process_message])

    def run(self):
        while True:
            try:
                self.consume()
            except self.conn.connection_errors:
                print("run(): connection errors")

    @staticmethod
    def process_message(body, message):
        # _, instance_cls, message_type = message.delivery_info["routing_key"].split(".")
        print("Got message: %s", message)
        print("send to kafka: %s", body)
        kafka_producer.send(body)
        message.ack()

    def consume(self):
        new_conn = self.establish_connection()
        while True:
            try:
                #print("consuming")
                new_conn.drain_events(timeout=2)
            except socket.timeout:
                #print("socket timeout")
                new_conn.heartbeat_check()

    def establish_connection(self):
        revived_connection = self.conn.clone()
        revived_connection.ensure_connection(max_retries=3)
        channel = revived_connection.channel()
        self.consumer.revive(channel)
        self.consumer.consume()
        return revived_connection
