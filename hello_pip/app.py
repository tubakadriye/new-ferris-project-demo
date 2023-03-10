import os
from ferris_ef import context

package_list= context.config.get('PACKAGE_LIST')

os.system("pip3 install {package_list}")
print("Libraries installed")