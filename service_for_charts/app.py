## From the terminal where you run your script, before you run, do
## export REQUESTS_CA_BUNDLE=/Users/tubakaraca/FerrisRootCA.pem
## export SSL_CERT_FILE=/Users/tubakaraca/FerrisRootCA.pem

from flask import Flask, jsonify, render_template, request
import json
from kafka import KafkaConsumer
import os
import time
import logging
import colorsys
import random
from minio import Minio
from minio.error import S3Error

# Configure the query to get the chart type
payload = json.loads(sys.argv[1])
chart_type = payload['chart_type']

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

print("Templates folder path:", os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

app = Flask(__name__)

is_running = True


distinct_colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    "#aec7e8", "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5", "#c49c94", "#f7b6d2", "#c7c7c7", "#dbdb8d", "#9edae5",
    "#393b79", "#8ca252", "#d6616b", "#7b4173", "#b5cf6b", "#ce6dbd", "#bd9e39", "#e7969c", "#e7ba52", "#31a354"
]

# Configure MinIO client
minioClient = Minio(
    "minio.ferris.ai",
    access_key="demo",
    secret_key="ferrisdemo123",
    secure=True
)

""" @app.route('/api/data', methods=['GET'])
def get_data():
    logger.info('inside api/data')
    chart_type = request.args.get('chart_type', default='pie', type=str)
    data = fetch_data_from_kafka(chart_type)
    return jsonify(data) """

""" @app.route('/')
def index():
    return render_template('index.html') """



def fetch_data_from_kafka(chart_type):
    time.sleep(1)
    global is_running
    consumer = KafkaConsumer(
        'esg-news',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest',  # Start reading from the beginning of the topic
        consumer_timeout_ms=10000 # stop listening after 10s, otherwise loop doesn't exit
    )

    data = {}

    if chart_type == 'pie':
        data = {
            "data": {
                "datasets": [
                    {
                        "backgroundColor": [],
                        "data": []
                    }
                ],
                "labels": []
            },
            "title": "ESG_News_Screen_Pie_Chart",
            "type": "pie"
        }

    elif chart_type == 'line':
        data = {
            "data": {
                "datasets": [
                    {
                        "backgroundColor": [] ,#distinct_colors[0],
                        "borderColor": [] , # distinct_colors[0],
                        "data": [], #[random.randint(0, 100) for _ in range(7)],
                        "fill": True,
                        "label": "triggered"
                    },
                    {
                        "backgroundColor": distinct_colors[1],
                        "borderColor": distinct_colors[1],
                        "data": [random.randint(0, 100) for _ in range(7)],
                        "fill": True,
                        "label": "scheduled"
                    },
                    {
                        "backgroundColor": distinct_colors[2],
                        "borderColor": distinct_colors[2],
                        "data": [random.randint(0, 100) for _ in range(7)],
                        "fill": True,
                        "label": "manual"
                    }
                ],
                "labels": [f"0{i}-06-22" for i in range(1, 8)]
            },
            "title": "ESG_News_Screen_Line_Chart",
            "type": "line"
        }

    elif chart_type == 'table':
        data = {
            "columns": [
                {
                    "field": "source_name",
                    "title": "Source Name"
                },
                {
                    "field": "count",
                    "title": "Count"
                }
            ],
            "data": [
                # """ {
                #     "count": random.randint(1, 100),
                #     "source_name": f"Source {i}"
                # } for i in range(1, 6) """
            ],
            "title": "ESG_News_Screen_Table_Chart",
            "type": "table"
        }

    for message in consumer:
        try:
            event = message.value
        except ValueError:
            logger.info(f"Invalid JSON message received: {message.value}")
            continue

        logger.info(f"Event received: {event}")

        source_name = event['source']['name']

        if chart_type == 'pie':
            #print('hello')
            #print(data)
            #print(data['data'])
            if source_name not in data['data']['labels']:
                print('hello')
                data['data']['labels'].append(source_name)
                data['data']['datasets'][0]['data'].append(1)
                color_index = len(data['data']['labels']) - 1
                data['data']['datasets'][0]['backgroundColor'].append(distinct_colors[color_index % len(distinct_colors)])
            else:
                index = data['data']['labels'].index(source_name)
                data['data']['datasets'][0]['data'][index] += 1

        elif chart_type == 'line':
            # Code for line chart
            pass

        elif chart_type == 'table':
            if source_name not in [row['source_name'] for row in data['data']]:
                data['data'].append({
                    "source_name": source_name,
                    "count": 1
                })
            else:
                index = next(i for i, row in enumerate(data['data']) if row['source_name'] == source_name)
                data['data'][index]['count'] += 1

    consumer.close()

    return data


def upload_to_minio(chart_type):
    data = fetch_data_from_kafka(chart_type)
    file_name = f"{chart_type}_chart.json"
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, "w") as f:
        json.dump(data, f)

    with open(file_path, "rb") as f:
        try:
            minioClient.put_object("ferris-home", file_name, f, length=os.path.getsize(file_path))
            print(f"JSON file {file_name} uploaded to MinIO.")
        except S3Error as exc:
            print(f"Error uploading JSON file {file_name} to MinIO: {exc}")

def get_minio_url(chart_type):
    file_name = f"{chart_type}_chart.json"
    try:
        url = minioClient.presigned_get_object("ferris-home", file_name)
        print(f"URL for {file_name}: {url}")
        return url
    except S3Error as exc:
        print(f"Error generating URL for {file_name}: {exc}")


upload_to_minio("pie")
url = get_minio_url("pie")

upload_to_minio("line")
url = get_minio_url("line")

upload_to_minio("table")
url = get_minio_url("table")

@app.route('/')
def index():
    logger.info('inside index')
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)