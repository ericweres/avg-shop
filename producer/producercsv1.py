#!/usr/bin/env python
import os
import sys
import csv
import random
import time
import pika

print("Producer1 gestartet")
def main():
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
                exchange='shop', routing_key=row[0], body=row[1]+","+row[2])
            print(f"Nachricht abgeschickt {row[0]}:{row[2]}")
            time.sleep(random.random())
    
    channel.exchange_declare(exchange='shop', exchange_type='direct')

    #Queue durable gesetzt, damit Bestellbestätigungen nicht verloren gehen
    result = channel.queue_declare(queue='producer1', durable=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='shop', queue=queue_name, routing_key="prod1")

    print(' [*] Warte auf Bestellbestätigungen. Zum Beenden drücke CTRL+C')

    #Ausgabe wenn Bestellung erhalten (hier könnte man auch Nachrichten zurück an Producer schicken)
    def callback(ch, method, properties, body):
        print(f" [x] Bestellbestätigungen erhalten {method.routing_key}:{body.decode()}")


    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
