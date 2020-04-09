import os
from os.path import dirname, join, splitext


module_dir = dirname(__file__)
modules_folder = join(module_dir, 'modules')

for cur_dir, sub_dirs, files_in_dir in os.walk(modules_folder):
    for cur_file in files_in_dir:
        module_num = splitext(cur_file)[0][-1]

        cur_file_path = join(cur_dir, cur_file)
        with open(cur_file_path, 'r') as file:
            code = file.read()
            
        new_code = code.replace('MyClass', 'MyClass' + module_num)

        with open(cur_file_path, 'w') as file:
            file.write(new_code)


















