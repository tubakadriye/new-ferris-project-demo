import sys
import json

payload = json.loads(sys.args[1])
print(payload)
print('I am step 2')