'''
An example script that shows how configuration from config.json file can be accessed from a script. service_name will be passed to the script as argument and then can be used for fetching configuration using ApplicationConfigurator from ferris_cli python service.
'''

import sys, json
from ferris_cli.v2 import ApplicationConfigurator

fa = json.loads(sys.argv[1])

service_name = fa['service_name']
config = ApplicationConfigurator.get(service_name)


for k,v in config.items():
    print(f"{k} -> {v}")
    print(v)