import sys
import json

from ferris_cli import EventSender

event_type = "my_custom_event_type"
data = {"some_parameter" : "Hello from Hello World"}

EventSender().send(event_type.data)