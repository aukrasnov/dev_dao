import pika
import sys
import time


# print('\n'.join(sys.argv[1:]))
# exit()
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    for i in range(5):
        time.sleep(1)
        print('.', end='', flush=True)
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='workshop',
                         exchange_type='topic')
channel.queue_declare(queue='all')
channel.queue_bind(exchange='workshop', queue='all', routing_key='type.*')

channel.basic_consume(queue='all',
                      auto_ack=False,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# * словл
# ничего или много слов