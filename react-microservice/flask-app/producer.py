import json

import pika

rabbit_url = 'amqps://cgmvablb:dD6bpmk8AkEeox7FbwYCGqGp-9gaajL7@shark.rmq.cloudamqp.com/cgmvablb'
params = pika.URLParameters(rabbit_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    print("publishing from main: ", body, properties)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body),
                          properties=properties)
