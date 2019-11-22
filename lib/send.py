import pika


class Singleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

class RabbitMQConfigure(metaclass=Singleton):

    def __init__(self, queue, host, routing_key, exchange=""):
        self.queue = queue
        self.host = host
        self.routing_key = routing_key
        self.exchange = exchange


class RabbitMQ():

    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def publish(self, payload={}):
        self._channel.basic_publish(
            exchange="",
            routing_key="hello",
            body=str(payload)
        )
        print("Published {}".format(payload))
        self._connection.close()

if __name__ == "__main__":
    server = RabbitMQConfigure(
        queue="Hello World",
        host="localhost",
        routing_key="hello",
        exchange=""
    )
    rabbitmq = RabbitMQ(server)
    rabbitmq.publish(payload={"data": "This is a test"})