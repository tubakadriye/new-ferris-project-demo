import json
import sys
import requests
import datetime
from kafka import KafkaProducer
from ferris_ef import context

# Configure the News API endpoint and API key
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/everything'
# newsapi_key = context.secrets.get('NEWS_API_KEY')
newsapi_key = '470b0ff17b994482bf1f4eacb76d11eb'
# Configure the Kafka broker endpoint and topic
KAFKA_BROKER_ENDPOINT = 'kafka.core:9092'
KAFKA_TOPIC = 'esg-news'

# Configure the search query to fetch news mentioning Zurich
payload = json.loads(sys.argv[1])
query = payload['keywords']

today = datetime.date.today()

# Calculate the date for yesterday
yesterday = today - datetime.timedelta(days=15)

# Fetch news articles using the News API
response = requests.get(NEWS_API_ENDPOINT, params={
    'q': query,
    'from': yesterday.isoformat(),
    'apiKey': newsapi_key
})

print('Response object type: ', type(response.text), len(response.text))

# Extract news articles from the response
articles = response.json()['articles']

# Create a Kafka producer instance
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_ENDPOINT)

# Publish each news article to the Kafka topic
for article in articles:
    # print(article)
    article_json = json.dumps(article)
    producer.send(KAFKA_TOPIC, value=article_json.encode('utf-8'))

# Close the Kafka producer
producer.close()






# Create a Kafka consumer instance
from kafka import KafkaConsumer
import json

KAFKA_BROKER_ENDPOINT = 'localhost:9092'
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
