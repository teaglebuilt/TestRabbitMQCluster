from kazoo.client import KazooClient
import logging
logging.basicConfig()



from kazoo.client import KazooClient

hosts = ["localhost:2181/esindicesLearn"]
# PATH = "/RabbitMQCluster/partOne"

print("creating client")
zk = KazooClient(hosts=hosts)

print("starting")
zk.start()



print("Stopping")
zk.stop()
