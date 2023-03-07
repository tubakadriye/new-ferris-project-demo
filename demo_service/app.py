import sys
import json

from ferris_cli.ferri_cli import ApplicationConfigurator
from ferris_cli.v2 import FerrisEvents

event_type = "my_custom_event_type"
data = {"some_parameter" : "Hello from Hello World"}

FerrisEvents().send(event_type.data)