import sys
import json
from my_class import MyClass

payload = json.loads(sys.argv[1])
MyClass().print_payload(payload)