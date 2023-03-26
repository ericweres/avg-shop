#!/usr/bin/env python
import pika
import csv
 


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='shop', exchange_type='direct')

with open('test.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        channel.basic_publish(
            exchange='shop', routing_key=row[0], body=row[1])
        print("Nachricht abgeschickt")
connection.close()
