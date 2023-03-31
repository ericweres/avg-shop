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
    result = channel.queue_declare(queue='hardware', durable=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='shop', queue=queue_name, routing_key="hw")

    print(' [*] Warte auf Bestellungen. Zum Beenden drücke CTRL+C')

    #Ausgabe wenn Bestellung erhalten (hier könnte man auch Nachrichten zurück an Producer schicken)
    def callback(ch, method, properties, body):
        content = body.decode()
        print(f" [x] Bestellung erhalten {method.routing_key}:{content}")
        channel.basic_publish(
            exchange='shop', routing_key=content.split(',')[0], body=content.split(',')[1])

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
