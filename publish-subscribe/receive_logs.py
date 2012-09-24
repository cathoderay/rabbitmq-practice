#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File: receive_logs.py
    Description: based on http://www.rabbitmq.com/tutorials/tutorial-three-python.html
"""

import pika


parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

# exclusive=True means queue deletion 
# when consumer is disconnected
result = channel.queue_declare(exclusive=True) 
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r" % (body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
