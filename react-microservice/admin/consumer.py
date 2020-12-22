import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

rabbit_url = 'amqps://cgmvablb:dD6bpmk8AkEeox7FbwYCGqGp-9gaajL7@shark.rmq.cloudamqp.com/cgmvablb'
params = pika.URLParameters(rabbit_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def admin_callback(ch, method, properties, body):
    print('Received in admin: ', body)
    id_data = json.loads(body)
    product = Product.objects.get(id=id_data)
    product.likes = product.likes + 1
    product.save()
    product = Product.objects.get(id=id_data)
    print("Product likes updated to ", product.likes)


channel.basic_consume(queue='admin', on_message_callback=admin_callback, auto_ack=True)

print('Started consuming in admin...')

channel.start_consuming()

channel.close()
