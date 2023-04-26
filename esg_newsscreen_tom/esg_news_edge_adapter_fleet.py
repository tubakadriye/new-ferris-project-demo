import json
import requests

from bs4 import BeautifulSoup
from ferris_sx.core import app
from ferris_sx.utils import sx_producer


print("Hello")

def count_keyword_mentions(url, keyword):
    # Make a request to the website
    response = requests.get(url)

    # Parse the HTML content of the website using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all instances of the keyword in the website content
    keyword_mentions = soup.find_all(text=lambda text: text and keyword in text)

    # Return the number of keyword mentions found
    return len(keyword_mentions)


def process(message):
    url = message['url']
    keyword = 'Zurich'

    mentions =count_keyword_mentions(url, keyword)

    message_new = dict()
    message_new['url'] = url
    message_new['mentions'] = mentions
    message_new_json = json.dumps(message_new)
    sx_producer.send(topic = "scope3_mentions", value = message_new_json.encode('utf-8'))
    print(message_new_json)


app.process = process











