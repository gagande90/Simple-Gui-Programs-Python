import os

module_dir = os.path.dirname(__file__)
backup_folder = os.path.join(module_dir, 'backup')

backup_files = os.listdir(backup_folder)
    
backup_files_path = [os.path.join(backup_folder, file) for file in backup_files]

try:
    for file in backup_files_path:
        os.remove(file)
except Exception as ex:
    print(ex)




















