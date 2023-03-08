import sys
import json
from ferris_cli.ferris_cli import ApplicationConfigurator

payload = json.loads(sys.argv[1])
print(payload)
print("I am step 2")

print('hello dx')

platform_config = ApplicationConfigurator().get("ferris.env")
print(platform_config)

platform_config_demo = ApplicationConfigurator().get("demoapp.env")
print(platform_config_demo)

my_config = ApplicationConfigurator().get("ferris.services.hello_config.config")["my_config"]
print(my_config)

