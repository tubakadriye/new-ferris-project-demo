import sys
import json
from ferris_cli.ferris_cli import ApplicationConfigurator
from ferris_ef import context


print('hello dx')

platform_config = ApplicationConfigurator().get("ferris.env")
print(platform_config)

my_config = context.config.get("my_config")
print("my_config:" , my_config)


charts = ApplicationConfigurator.get().get("PROJECT_CHARTS", [])

formatted_urls = []

for ch in charts:
    ch['ENDPOINT'] = f"{ch['ENDPOINT']}&project_id={pk}"
    print(ch['ENDPOINT'], flush=True)
    formatted_urls.append(ch)

