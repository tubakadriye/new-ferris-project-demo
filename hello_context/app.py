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

print("------- Get Service State -------")
print(context.state.get())


print("------- Get Secret -------")
print(context.secrets.get("test_secret_1"))

print("------- Set Secret -------")
print(context.secrets.set("test_secret_4", {"pfkey":"platform val"}, "platform"))
print(context.secrets.set("test_secret_4", {"prjkey":"project val"}, "project"))

print("------- Get Secret test_secret_4 -------")
print(context.secrets.get("test_secret_4"))

