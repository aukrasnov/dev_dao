import pika
import sys
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='all')

channel.exchange_declare(exchange ='workshop',
                         exchange_type = 'topic' # создается правило которое управляет очередями, direct, topic, fun_out
                          )

channel.queue_bind(exchange ='workshop',
                   queue='all',
                   routing_key ='type.*')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    return body


channel.basic_consume(queue='all', #очередь
                      auto_ack=False, #посылаем, считает что сообщение принято только если только вернет true
                      on_message_callback=callback) #функция которая вызывается когда приходит сообщение

# print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
