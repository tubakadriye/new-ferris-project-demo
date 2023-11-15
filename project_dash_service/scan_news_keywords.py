import json
import sys
import requests
import datetime
from kafka import KafkaProducer, KafkaConsumer

NEWS_API_ENDPOINT = 'https://newsapi.org/v2/everything'
newsapi_key = '470b0ff17b994482bf1f4eacb76d11eb'
#KAFKA_BROKER_ENDPOINT = 'localhost:9092'
KAFKA_BROKER_ENDPOINT = 'kafka.core:9092'
KAFKA_TOPIC = 'esg-news'

