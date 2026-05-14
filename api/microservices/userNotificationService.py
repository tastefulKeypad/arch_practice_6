import pika
import json
import rabbitmq

class UserNotificationService:
    def __init__(self):
        self.self.rabbitClient = RabbitMQClient()
        self.EventAddUserListen()
        self.EventAddRentListen()
        self.EventFinalizeRent()

    def EventAddRentListen(self):
        def callback(ch, method, properties, body):
            print(f" [x] userNotificationService | EventAddUser | RECEIVED: {body}")
        self.rabbitClient.channel.exchange_declare(exchange='userEvents', exchange_type='fanout')
        result = self.rabbitClient.channel.queue_declare(queue='', exclusive=True)
        queueName = result.method.queue
        self.rabbitClient.channel.queue_bind(exchange='userEvents', queue=queueName)
        self.rabbitClient.channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)
        self.rabbitClient.channel.start_consuming()

    def EventAddRentListen(self):
        def callback(ch, method, properties, body):
            print(f" [x] userNotificationService | EventAddRent | RECEIVED: {body}")
        self.rabbitClient.channel.exchange_declare(exchange='rentEvents', exchange_type='fanout')
        result = self.rabbitClient.channel.queue_declare(queue='', exclusive=True)
        queueName = result.method.queue
        self.rabbitClient.channel.queue_bind(exchange='rentEvents', queue=queueName)
        self.rabbitClient.channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)
        self.rabbitClient.channel.start_consuming()
    
    def EventFinalizeRentListen(self):
        def callback(ch, method, properties, body):
            print(f" [x] userNotificationService | EventFinalizeRent | RECEIVED: {body}")
        self.rabbitClient.channel.queue_declare(queue='notifyUser', durable=True, arguments={'x-queue-type': 'quorum'})
        self.rabbitClient.channel.basic_consume(queue='notifyUser', on_message_callback=callback, auto_ack=True)
        self.rabbitClient.channel.start_consuming()
