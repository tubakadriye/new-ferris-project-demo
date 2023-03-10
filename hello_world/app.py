import sys
import json

from ferris_cli.ferris_cli import ApplicationConfigurator
from ferris_cli.v2 import FerrisEvents
from ferris_ef import get_param

event_type = "my_custom_event_type"
data = {"some_parameter" : "Hello from Hello World"}
event_source = get_param('package_name')


#sends this to kafka maybe
FerrisEvents().send(event_type=event_type, event_source=event_source, data=data)
