#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    File: worker.py
    Description: based on http://www.rabbitmq.com/tutorials/tutorial-two-python.html
"""

import time

import pika


parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep(body.count('.'))
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='hello')
channel.start_consuming()
