import os

cwd = os.getcwd()
print(cwd)
module_dir = os.path.dirname(__file__)

os.chdir(os.pardir)
print(os.getcwd())












