import pika

params = pika.URLParameters('amqps://cgmvablb:dD6bpmk8AkEeox7FbwYCGqGp-9gaajL7@shark.rmq.cloudamqp.com/cgmvablb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def admin_callback(ch, method, properties, body):
    print('Received in admin... ', body)


channel.basic_consume(queue='admin', on_message_callback=admin_callback, auto_ack=True)

print('Started consuming....')

channel.start_consuming()

channel.close()

