import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

msg = ' '.join(sys.argv[1:])


channel.exchange_declare(exchange ='workshop',
                         exchange_type = 'topic'
                         )

channel.basic_publish(exchange='workshop',
                      routing_key='type.info',
                      body='2')
channel.basic_publish(exchange='workshop',
                      routing_key='type.info',
                      body='1')
channel.basic_publish(exchange='workshop',
                      routing_key='type.info',
                      body='ops')
channel.basic_publish(exchange='workshop',
                      routing_key='type.info',
                      body='1000000000000')

connection.close()