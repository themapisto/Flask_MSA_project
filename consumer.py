import pika

params = pika.URLParameters('amqps://wjdihkuz:13LRz2uHVsbK80oPLnLmPfwwowPFbdBs@cougar.rmq.cloudamqp.com/wjdihkuz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(channel, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
