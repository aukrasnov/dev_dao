import pika
import sys
import time


# print('\n'.join(sys.argv[1:]))
# exit()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='workshop',
                         exchange_type='topic')
# channel.queue_declare(queue='info')
# channel.queue_declare(queue='all')
# channel.queue_bind(exchange='workshop', queue_name='all', routing_key='type.*')
# channel.queue_bind(exchange='workshop', queue_name='info', routing_key='type.info')


channel.basic_publish(exchange='workshop',
                      routing_key='type.info',
                      body='1')

time.sleep(3)

channel.basic_publish(exchange='workshop',
                      routing_key='type.info',
                      body='2')

time.sleep(3)

channel.basic_publish(exchange='workshop',
                      routing_key='type.info',
                      body='3')

time.sleep(3)

channel.basic_publish(exchange='workshop',
                      routing_key='type.info',
                      body='10000000000')

time.sleep(3)

channel.basic_publish(exchange='workshop',
                      routing_key='type.info',
                      body='Done')


time.sleep(10)
connection.close()

