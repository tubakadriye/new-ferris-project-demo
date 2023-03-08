import sys
import json
from ferris_cli.ferris_cli import ApplicationConfigurator
from ferris_ef import context

payload = json.loads(sys.argv[1])
print(payload)
print("I am step 2")

print('hello dx')

platform_config = ApplicationConfigurator().get("ferris.env")
print(platform_config)

my_config = context.config.get("my_config")
print("my_config:" , my_config)

