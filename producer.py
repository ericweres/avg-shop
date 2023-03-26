#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='shop', exchange_type='direct')

channel.basic_publish(
    exchange='shop', routing_key='hw', body='Intel i5-13600K')
print("Nachricht abgeschickt")
connection.close()
