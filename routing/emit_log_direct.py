#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File: emit_log_direct.py
    Description: based on http://www.rabbitmq.com/tutorials/tutorial-four-python.html 
"""

import sys

import pika


parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print " [x] Sent %r:%r" % (severity, message)
connection.close()
