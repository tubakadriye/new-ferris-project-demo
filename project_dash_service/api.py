from flask import Flask
from minio import Minio
from minio.error import S3Error
import json

with open('config.json') as config_file:
    config = json.load(config_file)

#Configure MinIO client
minioClient = Minio(
    "minio.ferris.ai",
    access_key="demo",
    secret_key="ferrisdemo123",
    secure = True
)

# Create the bucket if it doesn't exist

bucket_name = "ferris_dash"

try:
    if not minioClient.bucket_exists(bucket_name):
        minioClient.make_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' created.")
    else:
        print(f"Bucket '{bucket_name}' already exists.")
except S3Error as err:
    print(f"Error creating bucket: {err}")

app = Flask(__name__)


#..

@app.route('/api/ferris-dash/<service>/<chart_type>', methods = ['GET'])
def get_chart_json(service, chart_type):
    json_file_name = f"{chart_type}_chart.json"

    try:
        json_data = minioClient.get_object(bucket_name, json_file_name)
        json_content = json.load(json_data)
        return json_content
    except S3Error as err:
        print(f"Error fetching JSON file from MinIO:{err}")
        return jsonify ({"error": f"Error fetching JSON file for {chart_type} chart "}), 500
    

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5001, debug= True)