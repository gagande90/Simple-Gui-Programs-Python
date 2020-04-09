import os
import shutil

module_dir = os.path.dirname(__file__)
backup_folder = os.path.join(module_dir, 'backup')

module_file = os.path.basename(__file__)

shutil.copy(module_file, backup_folder)

print(os.listdir(backup_folder))



















