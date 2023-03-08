import sys
import json
from modularising.my_class import MyClass

payload = json.loads(sys.argv[1])
print(payload)

MyClass().print_payload(payload)