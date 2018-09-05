# -* coding:utf8 *-  
from pykafka import KafkaClient

host = '192.168.112.181:9092'
client = KafkaClient(hosts=host)

print client.topics

# 消费者  
topic = client.topics['my-topic']
consumer = topic.get_simple_consumer(consumer_group='test', auto_commit_enable=True, auto_commit_interval_ms=1,
                                     consumer_id='test')
for message in consumer:
    if message is not None:
        print message.offset, message.value