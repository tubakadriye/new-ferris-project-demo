import json
import sys
from ferris_ef import get_param

fa = json.loads(sys.argv[1])
for k,v in fa.items():
    print(k,v)


# Alternatively you can use the provided helper function.
my_parameter = get_param("package_id")

print("package_id", my_parameter)