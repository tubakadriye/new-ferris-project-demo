from ferris_cli.v2 import FerrisEvents
from ferris_ef import context, get_param
import json


event_type = context.params.get("sample_event_type")
event_source = context.package.name

data = json.loads(context.params.get("sample_payload"))

FerrisEvents().send(event_type, event_source, data=data)