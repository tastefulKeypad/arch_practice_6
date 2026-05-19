import pika, json, time
from rabbitmq import RabbitMQClient

def run():
    print(" [x] clientService | INITIALIZATION")
    clientServiceInstance = ClientService()
    while True:
        time.sleep(2)
        clientServiceInstance.EventAddUser()
        time.sleep(8)

class ClientService:
    def __init__(self):
        self.rabbitClient = RabbitMQClient()

    def EventAddUser(self):
        message = json.dumps({
            "userName": "Petya",
            "userSurname": "Testovich",
            "userEmail": "petya@testovich.test"})
        self.rabbitClient.channel.exchange_declare(exchange='userEvents', exchange_type='fanout')
        self.rabbitClient.channel.basic_publish(exchange='userEvents', routing_key='', body=message)
        print(f" [x] clientService | EventAddUser | SENT: {message}")
