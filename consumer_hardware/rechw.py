#!/usr/bin/env python
import os
import sys
import pika


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='shop', exchange_type='direct')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='shop', queue=queue_name, routing_key="hw")

    print(' [*] Warte auf Bestellungen. Zum Beenden drücke CTRL+C')


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