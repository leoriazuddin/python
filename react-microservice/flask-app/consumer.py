import json

from .main import Product, db
import pika

params = pika.URLParameters('amqps://cgmvablb:dD6bpmk8AkEeox7FbwYCGqGp-9gaajL7@shark.rmq.cloudamqp.com/cgmvablb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def main_callback(ch, method, properties, body):
    data = json.loads(body)
    print('Received in mainddd... ', data, properties)
    if properties.content_type == 'create':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        product = Product.query.get(data['id'])
        print("Created : ", product.id, product.image, product.title)
    elif properties.content_type == 'updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        product = Product.query.get(data['id'])
        print("Updated : ", product.id, product.image, product.title)
    elif properties.content_type == 'deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print("Deleted : ", product.id, product.image, product.title)


channel.basic_consume(queue='main', on_message_callback=main_callback, auto_ack=True)

print('Started mnew ain app consuming....')

channel.start_consuming()

channel.close()
