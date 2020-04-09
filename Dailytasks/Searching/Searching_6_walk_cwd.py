import os
from pprint import pprint


search_start_dir = os.getcwd()              # start search from cwd
print(search_start_dir)

walk_all = next(os.walk(search_start_dir))      
pprint(walk_all)




















