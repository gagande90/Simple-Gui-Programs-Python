import os

os.chdir(os.pardir)
search_start_dir = os.getcwd()              

dirs = []
files = []

for cur_dir, sub_dirs, files_in_dir in os.walk(search_start_dir):
    print('Current directory: {}'.format(cur_dir))
    if cur_dir.startswith('.'):
        continue
    dirs.append(cur_dir)
    for cur_file in files_in_dir:
        if cur_file.startswith('.'):
            continue        
        print('\t{}'.format(cur_file))
        files.append(cur_file)
          
print(dirs)
print(files)  
















