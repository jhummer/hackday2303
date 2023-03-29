# hackday2303

Hackday project handling a RabbitMQ -> Kafka transition.

Legacy services use RabbitMQ and Kafka is the "new" kid. We need a service to read legacy RabbitMQ messages and publish these to Kafka instead.

Project consists of following parts:

## base-services

Docker containers needed to run the project: 

- postgres
- rabbitmq 
- kafka

## vehicle-api

Django-ninja API publishing model events on RabbitMQ

Swagger:
http://localhost:8000/api/docs

## rabbit-kafka-worker

Service consuming RabbitMQ and publishing to Kafka
