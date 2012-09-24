#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    File: worker.py
    Description: based on http://www.rabbitmq.com/tutorials/tutorial-two-python.html
"""

import time

import pika


queue_name = "task_queue"
parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue=queue_name, durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep(body.count('.'))
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

# prefetch_count=1 promotes fair dispatch
channel.basic_qos(prefetch_count=1) 

channel.basic_consume(callback,
                      queue=queue_name)
channel.start_consuming()
