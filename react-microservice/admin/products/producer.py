import json

import pika

params = pika.URLParameters('amqps://cgmvablb:dD6bpmk8AkEeox7FbwYCGqGp-9gaajL7@shark.rmq.cloudamqp.com/cgmvablb')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    print("publishing....", properties)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body),
                          properties=properties)
