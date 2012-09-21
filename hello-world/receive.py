#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File: receive.py
    Description: based on http://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

import pika


parameters = pika.ConnectionParameteres('localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
