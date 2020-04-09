import os

cwd = os.getcwd()
module_dir = os.path.dirname(__file__)

full_path, curent_folder = os.path.split(module_dir)

print(full_path)
print(curent_folder)






















