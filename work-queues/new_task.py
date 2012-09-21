#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File: new_task.py
    Description: based on http://www.rabbitmq.com/tutorials/tutorial-two-python.html
"""

import sys

import pika


parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print " [x] Sent %r" % (message, )
connection.close()
