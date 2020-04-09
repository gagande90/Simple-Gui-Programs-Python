import os
from pprint import pprint

os.chdir(os.pardir)

search_start_dir = os.getcwd()
print(search_start_dir)

walk_all = next(os.walk(search_start_dir))      
pprint(walk_all)




















