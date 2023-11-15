import os
import json
import sys

payload = json.loads(sys.argv[1])
library_tbi = payload['library_to_be_installed']

os.system(f'python3 -m pip install {library_tbi}')
os.system('pip list')

print(f'{library_tbi} was installed')