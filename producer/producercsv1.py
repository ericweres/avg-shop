#!/usr/bin/env python
import csv
import random
import time
import pika

print("Producer 1 gestartet")
#Verbindung mit RabbitMQ Server aufbauen
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='shop', exchange_type='direct')

#Bestelldaten aus CSV Datei auslesen und als Nachricht versenden
with open('csv1.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        channel.basic_publish(
            exchange='shop', routing_key=row[0], body=row[1])
        print(f"Nachricht abgeschickt {row[0]}:{row[1]}")
        time.sleep(random.random())
connection.close()
