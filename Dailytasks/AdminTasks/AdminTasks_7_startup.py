import psutil                      
from datetime import datetime

print('STARTUP Related ----')
print(psutil.boot_time())
print(datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))














