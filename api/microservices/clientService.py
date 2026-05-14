import pika
import json
import rabbitmq

rabbitClient = RabbitMQClient()

def EventAddUser():
    message = json.dumps({
        "userName": "Petya"
        "userSurname": "Testovich"
        "userEmail": "petya@testovich.test"})
    rabbitClient.channel.exchange_declare(exchange='userEvents', exchange_type='fanout')
    rabbitClient.channel.basic_publish(exchange='userEvents', routing_key='', body=message)
    print(f" [x] clientService | EventAddUser | SENT: {message}")
