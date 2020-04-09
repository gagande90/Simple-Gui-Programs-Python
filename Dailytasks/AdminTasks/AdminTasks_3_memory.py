import os
import psutil                       

print('MEMORY via PROCESS ----')
p = psutil.Process()                                # current process
print(p)
print(os.getpid())                                  # get pid via os - same pid as return above
print(p.memory_info())
print('RSS/wset:', p.memory_info().rss)             # aka working set
print('VMS/pagefile:', p.memory_info().vms)         # pagefile


















