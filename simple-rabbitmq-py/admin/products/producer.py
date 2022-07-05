import json

import pika

params = pika.URLParameters("amqp://root:test@rabbitmq:5672")

connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties()
    channel.basic_publish(
        exchange="",
        routing_key="main",
        body=json.dumps(body),
        properties=properties
    )
