# Microservice Messaging Discovery

Its common for a messaging framework such as RabbitMQ, Kafka, or Redis to exist in a microservice framework. Typically to send and recieve events to other services. Zookeeper is another service commonly used for its wide availability of different use cases, ranging from service registry to synchronization, tracking events, and so on...

In this repo, im going to use Docker to spin up a 3 node cluster or RabbitMQ and Zookeeper. The purpose is to first learn how we can use rabbitmq, then learn how we can write automated tests to monitor these services.

##  Tools used...

*  Docker
*  Docker-Compose
*  RabbitMQ
*  Zookeeper
*  Python
*  RobotFramework
*  Shell



## Project Layout
--root
- lib/ -- classes for RabbitMQ/Zookeeper/other..
- test/ -- test suites
- rabbitmq.config -- configurations for rabbitmq
- definitions.json -- settings for rabbitmq
- 


###  Installation


#### Create Docker Network
```
docker network create rabbitmq-cluster

```

#### Launch containers

```
docker-compose up -d
```

#### virtual environment

```
virtualenv -p "{{ path to python version }}" env
```

activate env

```
source env/bin/activate

```

install dependencies

```
pip install -r requirements.txt
```


go to localhost:15672


