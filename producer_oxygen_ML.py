#!/usr/bin/env python
import time
import pika
from random import uniform

rabbit_host = '10.128.0.10'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'monitoring_measurements'
topic = 'ML.401.Oxygen'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

print('> Sending measurements. To exit press CTRL+C')

while True:
    value = round(uniform(0, 30), 1)
    payload = "{'value':%r,'unit':'O2'}" % (value)
    channel.basic_publish(exchange=exchange,
                          routing_key=topic, body=payload)
    print("Monitored Oxygen: %r" % (value))
    time.sleep(3)

connection.close()
