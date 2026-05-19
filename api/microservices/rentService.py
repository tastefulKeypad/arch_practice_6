import pika, json, time, sys
from rabbitmq import RabbitMQClient

def run():
    print(" [x] rentService | INITIALIZATION")
    rentServiceInstance = RentService()
    while True:
        time.sleep(3)
        rentServiceInstance.EventAddRent()
        time.sleep(2)
        rentServiceInstance.EventFinalizeRent()
        sys.stdout.flush()
        time.sleep(5)

class RentService:
    def __init__(self):
        self.rabbitClient = RabbitMQClient()

    def EventAddRent(self):
        message = json.dumps({
            "userId": 1,
            "carId": 1,
            "dateStart": "2026-01-01T00:00:00",
            "dateEnd": "2026-01-13T00:00:00",
            "status": "Active"})
        self.rabbitClient.channel.exchange_declare(exchange='rentEvents', exchange_type='fanout')
        self.rabbitClient.channel.basic_publish(exchange='rentEvents', routing_key='', body=message)
        print(f" [x] rentService | EventAddRent | SENT: {message}")
    
    def EventFinalizeRent(self):
        message = json.dumps({
            "userId": 1,
            "carId": 1,
            "dateStart": "2026-01-01T00:00:00",
            "dateEnd": "2026-01-13T00:00:00"})
        self.rabbitClient.channel.queue_declare(queue='notifyUser', durable=True, arguments={'x-queue-type': 'quorum'})
        self.rabbitClient.channel.basic_publish(exchange='', routing_key='notifyUser', body=message)
        print(f" [x] rentService | EventFinalizeRent | SENT: {message}")
