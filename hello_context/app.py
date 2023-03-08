import sys
import json
from ferris_ef import context

payload = json.loads(sys.argv[1])
print(payload)
print("I am step 2")

print('hello dx')



print("------- Get Service Config -------")
print(context.config.get("my_config"))

print("------- Get Execution Params -------")
print(json.dumps(context.params))

print("------- Get Service Info -------")
print(context.package.name)
print(context.package.id)

print("------- Get Service State -------")
print(context.state.get())

print("------- Update Service State -------")
context.state.put("some_key", "some_value")
context.state.put("other_key", {"attr_1": "val_1"})

