import pika, json, threading
from rabbitmq import RabbitMQClient

def run():
    print(" [x] userNotificationService | INITIALIZATION")
    userNotificationServiceInstance = UserNotificationService()

class UserNotificationService:
    def __init__(self):
        self.rabbitClient = RabbitMQClient()
        self.EventAddUserListen()
        self.EventAddRentListen()
        self.EventFinalizeRentListen()
        print(" [x] userNotificationService | READY")
        self.rabbitClient.channel.start_consuming()

    def EventAddUserListen(self):
        def callback(ch, method, properties, body):
            print(f" [x] userNotificationService | EventAddUser | RECEIVED: {body}")
        self.rabbitClient.channel.exchange_declare(exchange='userEvents', exchange_type='fanout')
        result = self.rabbitClient.channel.queue_declare(queue='', exclusive=True)
        queueName = result.method.queue
        self.rabbitClient.channel.queue_bind(exchange='userEvents', queue=queueName)
        self.rabbitClient.channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)

    def EventAddRentListen(self):
        def callback(ch, method, properties, body):
            print(f" [x] userNotificationService | EventAddRent | RECEIVED: {body}")
        self.rabbitClient.channel.exchange_declare(exchange='rentEvents', exchange_type='fanout')
        result = self.rabbitClient.channel.queue_declare(queue='', exclusive=True)
        queueName = result.method.queue
        self.rabbitClient.channel.queue_bind(exchange='rentEvents', queue=queueName)
        self.rabbitClient.channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)
    
    def EventFinalizeRentListen(self):
        def callback(ch, method, properties, body):
            print(f" [x] userNotificationService | EventFinalizeRent | RECEIVED: {body}")
        self.rabbitClient.channel.queue_declare(queue='notifyUser', durable=True, arguments={'x-queue-type': 'quorum'})
        self.rabbitClient.channel.basic_consume(queue='notifyUser', on_message_callback=callback, auto_ack=True)
