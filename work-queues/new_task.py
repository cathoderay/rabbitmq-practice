#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File: new_task.py
    Description: based on http://www.rabbitmq.com/tutorials/tutorial-two-python.html
"""

import sys

import pika


queue_name = "task_queue"
parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue=queue_name, durable=True)
message = ' '.join(sys.argv[1:]) or "Hello World!"
properties = pika.BasicProperties(delivery_mode=2) #2 to persist
channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=message,
                      properties=properties)

print " [x] Sent %r" % (message, )
connection.close()
