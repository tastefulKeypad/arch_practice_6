import pika, json, threading
from rabbitmq import RabbitMQClient

def run():
    print(" [x] analyticsService | INITIALIZATION")
    analyticsServiceInstance = AnalyticsService()

class AnalyticsService:
    def __init__(self):
        self.rabbitClient = RabbitMQClient()
        self.EventAddUserListen()
        self.EventAddRentListen()
        print(" [x] analyticsService | READY")
        self.rabbitClient.channel.start_consuming()

    def EventAddUserListen(self):
        def callback(ch, method, properties, body):
            print(f" [x] analyticsService | EventAddUser | RECEIVED: {body}")
        self.rabbitClient.channel.exchange_declare(exchange='userEvents', exchange_type='fanout')
        result = self.rabbitClient.channel.queue_declare(queue='', exclusive=True)
        queueName = result.method.queue
        self.rabbitClient.channel.queue_bind(exchange='userEvents', queue=queueName)
        self.rabbitClient.channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)

    def EventAddRentListen(self):
        def callback(ch, method, properties, body):
            print(f" [x] analyticsService | EventAddRent | RECEIVED: {body}")
        self.rabbitClient.channel.exchange_declare(exchange='rentEvents', exchange_type='fanout')
        result = self.rabbitClient.channel.queue_declare(queue='', exclusive=True)
        queueName = result.method.queue
        self.rabbitClient.channel.queue_bind(exchange='rentEvents', queue=queueName)
        self.rabbitClient.channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)
