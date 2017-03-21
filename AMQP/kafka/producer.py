from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.33.10:9092')

for _ in range(100):
	producer.send('foobar', b'some_message_bytes')
	print "send one complete"