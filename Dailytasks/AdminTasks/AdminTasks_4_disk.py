import psutil                       
import shutil

print('DISK Related ----')
print(psutil.disk_partitions())             # [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='FAT32', opts='rw,removable')]

print(psutil.disk_usage('/'))               # sdiskusage(total=987588718592, used=163852578816, free=823736139776, percent=16.6)

print('C:', shutil.disk_usage('C://'))      # similar info via shell utility
print('D:', shutil.disk_usage('D://'))




























