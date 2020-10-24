import pika
import sys

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
                      routing_key='type.error',
                      body='ValueError')

channel.basic_publish(exchange='workshop',
                      routing_key='type.info',
                      body='Done')

channel.basic_publish(exchange='workshop',
                      routing_key='type.critical',
                      body=' CRITICAL AAAAAAAA!!!!')


connection.close()

