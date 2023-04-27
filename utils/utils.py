import os

os.system(f'python3 -m pip install bs4')
os.system(f'python3 -m pip install ferris_sx')
os.system('pip list')

print('list was installed')

print(os.environ['APP_NAME'])
print(os.environ['TOPIC_NAME'])
print(os.environ['MODULE_NAME'])
print(os.environ['CLASS_NAME'])
print(os.environ['BATCH_NUMBER'])
print(os.environ['BATCH_FRAME'])
print(os.environ['KAFKA_NODES'])
print(os.environ['LOG_TO_KAFKA_LEVEL'])