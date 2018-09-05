# -* coding:utf8 *-
from pykafka import KafkaClient

host = '192.168.112.181:9092'
client = KafkaClient(hosts=host)

print client.topics

# 生产者
topicdocu = client.topics['my-topic']
producer = topicdocu.get_producer()
for i in range(10000000):
    print i
    producer.produce('test message ' + str(i ** 2))
producer.stop()