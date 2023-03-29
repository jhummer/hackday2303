import logging

from django.conf import settings
from kombu import Connection, Exchange, Queue

log = logging.getLogger(__name__)


class Publisher:
    """Publishes messages to RabbitMQ"""

    @classmethod
    def publish(cls, model, message, status):
        """
        Publish a message to RabbitMQ
        :param model: model name
        :param message: dict representation of instance
        :param status: routing_key status suffix (added/updated/deleted)
        :return: None
        """
        routing_key = f"vehicle.{model}.{status}"
        if not settings.RMQ_PUBLISH_ENABLED:
            log.debug("skipping publish to %s", routing_key)
            return

        exchange = Exchange("vehicle", type="topic", durable=True)
        queue = Queue(name="vehicle", exchange=exchange, routing_key="vehicle.*.*")

        with Connection(settings.RMQ_CONNSTR, heartbeat=10) as conn:
            channel = conn.channel()
            queue(channel).declare()
            producer = conn.Producer(
                serializer="json",
                exchange=exchange,
                channel=channel,
                routing_key=routing_key
            )
            producer.publish(message)
            log.debug("published %s: %s", routing_key, message)
