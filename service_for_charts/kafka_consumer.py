from kafka import KafkaConsumer
import json

#KAFKA_BROKER_ENDPOINT = 'localhost:9092'
KAFKA_BROKER_ENDPOINT = 'kafka.core:9092'
KAFKA_TOPIC = 'esg-news'

# Create a Kafka consumer instance
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER_ENDPOINT,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest'  # Start reading from the beginning of the topic
)

# Print the messages received from the Kafka topic
for message in consumer:
    print("Message: ", message.value)
