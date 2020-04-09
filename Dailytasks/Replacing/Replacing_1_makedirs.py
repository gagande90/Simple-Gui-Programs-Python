import os
from pprint import pprint

module_dir = os.path.dirname(__file__)
pprint(os.listdir(module_dir))

backup_folder = os.path.join(module_dir, 'backup')

os.makedirs(backup_folder, exist_ok=True)

pprint(os.listdir(module_dir))






















