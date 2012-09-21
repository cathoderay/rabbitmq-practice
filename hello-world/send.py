#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File: send.py
    Description: based on http://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

import pika


parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
