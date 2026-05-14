import pika, os

class RabbitMQClient:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.connect()

    def __del__(self):
        self.close()

    def connect(self):
        hostname = os.getenv('RABBITMQ_HOST', 'arch_practice_6_rabbitmq')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname))
        self.channel = self.connection.channel()

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
