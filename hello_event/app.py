import sys
import json
from ferris_cli.v2 import FerrisEvents
from ferris_ef import get_param

def hello_world(payload):
    print(payload)

payload = json.loads(sys.arg[1])

hello_world(payload)


""" event_type = "my_custom_event_type"
event_source = get_param('package_name')
data = {"some_parameter":"Hello from Hello World"}
FerrisEvents().send(event_type=event_type, event_source=event_source, data=data) """