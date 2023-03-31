#!/usr/bin/env python
import os
import sys
import pika

print("Hardware Consumer gestartet")
def main():
    #Verbindung mit RabbitMQ Server aufbauen
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='shop', exchange_type='direct')

    #Queue durable gesetzt, damit Bestellbestätigungen nicht verloren gehen
    result = channel.queue_declare(queue='software', durable=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='shop', queue=queue_name, routing_key="sw")

    print(' [*] Warte auf Bestellungen. Zum Beenden drücke CTRL+C')

    #Ausgabe wenn Bestellung erhalten (hier könnte man auch Nachrichten zurück an Producer schicken)
    def callback(ch, method, properties, body):
        print(f" [x] Bestellung erhalten {method.routing_key}:{body.decode()}")

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
