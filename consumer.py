import pika

params = pika.URLParameters('amqps://wjdihkuz:13LRz2uHVsbK80oPLnLmPfwwowPFbdBs@cougar.rmq.cloudamqp.com/wjdihkuz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(channel, method, properties, body):
    print('Received in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()