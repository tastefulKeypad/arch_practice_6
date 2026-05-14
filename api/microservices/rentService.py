import pika
import json
from rabbitmq import RabbitMQClient

rabbitClient = RabbitMQClient()

def EventAddRent():
    message = json.dumps({
        "userId": 1,
        "carId": 1,
        "dateStart": "2026-01-01T00:00:00",
        "dateStart": "2026-01-13T00:00:00",
        "status": "Active"})
    rabbitClient.channel.exchange_declare(exchange='rentEvents', exchange_type='fanout')
    rabbitClient.channel.basic_publish(exchange='rentEvents', routing_key='', body=message)
    print(f" [x] rentService | EventAddRent | SENT: {message}")

def EventFinalizeRent():
    message = json.dumps({
        "userId": 1,
        "carId": 1,
        "dateStart": "2026-01-01T00:00:00",
        "dateStart": "2026-01-13T00:00:00"})
    rabbitClient.channel.queue_declare(queue='notifyUser', durable=True, arguments={'x-queue-type': 'quorum'})
    rabbitClient.channel.basic_publish(exchange='', routing_key='notifyUser', body=message)
    print(f" [x] rentService | EventFinalizeRent | SENT: {message}")
