#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File: emit_log.py
    Description: based on http://www.rabbitmq.com/tutorials/tutorial-three-python.html
"""

import sys

import pika


queue_name = "name"
parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print " [x] Sent %r" % (message, )
connection.close()
