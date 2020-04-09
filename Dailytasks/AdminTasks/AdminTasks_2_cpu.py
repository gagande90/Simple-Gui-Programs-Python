'''
Created on May 13, 2018
@author: Burkhard A. Meier
'''








#-----------------------------------------
# https://psutil.readthedocs.io/en/latest/        <=== study this 'read the docs' site
#-----------------------------------------

import psutil 

print('CPU Related ----')
print('CPU utilization %:',  psutil.cpu_percent(interval=1))       # interval=1 blocking, default is non-blocking 
print('CPU number of logical processors:', psutil.cpu_count())                   
print('CPU number of cpu cores:', psutil.cpu_count(logical=False))      




















