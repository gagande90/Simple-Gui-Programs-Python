import psutil                       
import shutil

print('DISK Related ----')
for partition in psutil.disk_partitions():
    print(partition)

























