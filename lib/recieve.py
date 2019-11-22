import pika
import ast


class Singleton(type):

    _instance ={}

    def __call__(cls, *args, **kwargs):

        """ Singelton Design Pattern  """

        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitMqServerConfigure(metaclass=Singleton):

    def __init__(self, host, queue):
        self.host = host
        self.queue = queue


class Server():

    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    @staticmethod
    def callback(ch, method, properties, body):
        payload = body.decode("utf-8")
        payload = ast.literal_eval(payload)
        print(type(payload))
        print("Data Recieved: {}".format(payload))

    def start_server(self):
        self._channel.basic_consume(
            queue=self.server.queue,
            on_message_callback=Server.callback,
            auto_ack=True
        )
        print("Listening..")
        self._channel.start_consuming()



if __name__ == "__main__":
    settings = RabbitMqServerConfigure(host='localhost', queue='hello')
    server = Server(server=settings)
    server.start_server()
