import sys
import json
from ferris_cli.ferris_cli import ApplicationConfigurator
from ferris_ef import context
from pydoc import locate


print('hello dx')

platform_config = ApplicationConfigurator().get("ferris.env")
print(platform_config)

"""my_config = context.config.get("my_config")
print("my_config:" , my_config) """


related_views = []

for rel_view in ApplicationConfigurator().get().get('PROJECTS_RELATED_VIEWS', []):
    print(rel_view, flush=True)
    cls = locate(rel_view)
    related_views.append(cls)



#charts = ApplicationConfigurator.get().get("PROJECT_CHARTS", [])



#formatted_urls = []

""" for ch in charts:
    ch['ENDPOINT'] = f"{ch['ENDPOINT']}&project_id={pk}"
    print(ch['ENDPOINT'], flush=True)
    formatted_urls.append(ch) """




    

