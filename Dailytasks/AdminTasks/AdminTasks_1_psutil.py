import os
import psutil                       # pip install psutil
import shutil
from datetime import datetime


#-----------------------------------------
# https://psutil.readthedocs.io/en/latest/        <=== study this 'read the docs' site
#-----------------------------------------

print('CPU Related ----')
print(psutil.cpu_percent(interval=1))       # interval=1 blocking 
print(psutil.cpu_count())                   # 4 logical processors   
print(psutil.cpu_count(logical=False))      # 2 cpu cores
print()

print('MEMORY Related ----')
p = psutil.Process()
print(p.memory_info())
print('RSS/wset:', p.memory_info().rss)
print('VMS/pagefile:', p.memory_info().vms)
print() 

print('DISK Related ----')
print(psutil.disk_partitions())             # [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='FAT32', opts='rw,removable')]
print(psutil.disk_usage('/'))               # sdiskusage(total=987588718592, used=163852578816, free=823736139776, percent=16.6)
print('C:', shutil.disk_usage('C://'))      # or: print(shutil.disk_usage('/'))     
print('D:', shutil.disk_usage('D://'))
print()

print('PROCESS Related ----')
print('pid:', os.getpid())              # get the current process id
print(psutil.Process())                 # if not pid passed in, will use the current pid
print()

print('BATTERY Related ----')
def from_seconds(seconds):
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
#     return "%d:%02d:%02d" % (hours, mins, secs)
    return '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

battery = psutil.sensors_battery()
print(battery)
print('Battery charge= {}%, Battery time left= {}'.format(battery.percent, from_seconds(battery.secsleft)))
'''
sbattery(percent=100, secsleft=<BatteryTime.POWER_TIME_UNLIMITED: -2>, power_plugged=True)
charge = 100%, time left = -1:59:58
'''
print()

print('BOOT Related ----')
print(psutil.boot_time())
print(datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

''' THIS IS GOOD
1526146521.0            from timestamp
2018-05-12 13:35:21      <==
'''
print()




def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def main1():
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))


# if __name__ == '__main__':
#     sys.exit(main1())
    
'''
Device               Total     Used     Free  Use %      Type  Mount
C:\                 919.8G   152.6G   767.2G    16%      NTFS  C:\
D:\                 115.7G    38.8G    76.8G    33%     FAT32  D:\
'''    


# print(psutil.disk_io_counters())    # sdiskio(read_count=1163276, write_count=1505739, read_bytes=22141272576, write_bytes=24538789888, read_time=9402, write_time=1747)
# 
# print(psutil.net_io_counters())     # snetio(bytes_sent=23589706, bytes_recv=223573588, packets_sent=129332, packets_recv=219365, errin=0, errout=0, dropin=0, dropout=0)
# 
# print(psutil.net_connections())     # [sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53786), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=7779), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=49664), raddr=(), status='NONE', pid=3532), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.101', port=62150), raddr=(), status='NONE', pid=3532), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=50154), raddr=(), status='LISTEN', pid=6596), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53776), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5050), raddr=(), status='NONE', pid=6192), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53763), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49665), raddr=(), status='LISTEN', pid=1356), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53777), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=445), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5355), raddr=(), status='NONE', pid=2540), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53787), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=139), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=500), raddr=(), status='NONE', pid=3508), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53761), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.101', port=59576), raddr=(), status='NONE', pid=4764), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=49947), raddr=(), status='NONE', pid=4688), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53758), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=50151), raddr=addr(ip='127.0.0.1', port=50152), status='ESTABLISHED', pid=6596), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=50151), raddr=(), status='LISTEN', pid=6596), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=63054), raddr=(), status='NONE', pid=11128), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.101', port=137), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=135), raddr=(), status='LISTEN', pid=76), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=50152), raddr=addr(ip='127.0.0.1', port=50151), status='ESTABLISHED', pid=12280), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::1', port=49945), raddr=(), status='NONE', pid=4688), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49688), raddr=(), status='LISTEN', pid=908), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=135), raddr=(), status='LISTEN', pid=76), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=3544), raddr=(), status='NONE', pid=3532), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53772), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=50155), raddr=addr(ip='127.0.0.1', port=50154), status='ESTABLISHED', pid=4992), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=1900), raddr=(), status='NONE', pid=4688), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=4500), raddr=(), status='NONE', pid=3508), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49671), raddr=(), status='LISTEN', pid=924), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=5040), raddr=(), status='LISTEN', pid=6192), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=7779), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='2604:2000:1101:14a:50e6:211e:267b:7f5b', port=53567), raddr=addr(ip='2606:2800:11f:17a5:191a:18d5:537:22f9', port=443), status='CLOSE_WAIT', pid=1060), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=50154), raddr=(), status='LISTEN', pid=6596), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53765), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=56680), raddr=(), status='NONE', pid=3304), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53788), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53762), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=49672), raddr=addr(ip='52.165.175.144', port=443), status='ESTABLISHED', pid=3928), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53755), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=3702), raddr=(), status='NONE', pid=3304), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53760), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5353), raddr=(), status='NONE', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5353), raddr=(), status='NONE', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53757), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53767), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=4500), raddr=(), status='NONE', pid=3508), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=3702), raddr=(), status='NONE', pid=3304), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=56681), raddr=(), status='NONE', pid=3304), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=445), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=3648), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::1', port=1900), raddr=(), status='NONE', pid=4688), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=49670), raddr=(), status='LISTEN', pid=4764), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.101', port=1900), raddr=(), status='NONE', pid=4688), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49688), raddr=(), status='LISTEN', pid=908), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53764), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=3306), raddr=(), status='LISTEN', pid=3644), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49666), raddr=(), status='LISTEN', pid=1692), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=6646), raddr=(), status='NONE', pid=5036), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49666), raddr=(), status='LISTEN', pid=1692), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::f1bb:8b87:4811:33bb', port=49944), raddr=(), status='NONE', pid=4688), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=63054), raddr=(), status='NONE', pid=11128), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53756), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49665), raddr=(), status='LISTEN', pid=1356), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49664), raddr=(), status='LISTEN', pid=764), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53766), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53785), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53778), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.101', port=1900), raddr=(), status='NONE', pid=4764), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53774), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5355), raddr=(), status='NONE', pid=2540), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.101', port=59577), raddr=(), status='NONE', pid=4764), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53768), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53769), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49671), raddr=(), status='LISTEN', pid=924), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49667), raddr=(), status='LISTEN', pid=3032), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.101', port=49946), raddr=(), status='NONE', pid=4688), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49664), raddr=(), status='LISTEN', pid=764), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53773), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53775), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5353), raddr=(), status='NONE', pid=2540), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5353), raddr=(), status='NONE', pid=2540), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49667), raddr=(), status='LISTEN', pid=3032), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=50151), raddr=(), status='LISTEN', pid=6596), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=500), raddr=(), status='NONE', pid=3508), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53759), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=50154), raddr=addr(ip='127.0.0.1', port=50155), status='ESTABLISHED', pid=6596), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53771), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.101', port=53770), raddr=addr(ip='151.101.0.133', port=443), status='ESTABLISHED', pid=9372), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=3306), raddr=(), status='LISTEN', pid=3644), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::f1bb:8b87:4811:33bb', port=1900), raddr=(), status='NONE', pid=4688), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.101', port=138), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=3648), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=6646), raddr=(), status='LISTEN', pid=5036)]

import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

AD = "-"
AF_INET6 = getattr(socket, 'AF_INET6', object())
proto_map = {
    (AF_INET, SOCK_STREAM): 'tcp',
    (AF_INET6, SOCK_STREAM): 'tcp6',
    (AF_INET, SOCK_DGRAM): 'udp',
    (AF_INET6, SOCK_DGRAM): 'udp6',
}


def main():
    templ = "%-5s %-30s %-30s %-13s %-6s %s"
    print(templ % (
        "Proto", "Local address", "Remote address", "Status", "PID",
        "Program name"))
    proc_names = {}
    for p in psutil.process_iter(attrs=['pid', 'name']):
        proc_names[p.info['pid']] = p.info['name']
    for c in psutil.net_connections(kind='inet'):               # C onnection
        laddr = "%s:%s" % (c.laddr)                             # L ocal
        raddr = ""                                              # R emote
        if c.raddr:
            raddr = "%s:%s" % (c.raddr)
        print(templ % (
            proto_map[(c.family, c.type)],
            laddr,
            raddr or AD,
            c.status,
            c.pid or AD,
            proc_names.get(c.pid, '?')[:15],
        ))


# if __name__ == '__main__':
#     main()

''' and many more results
Proto Local address                  Remote address                 Status        PID    Program name
tcp   192.168.1.101:53842            54.172.78.33:443               ESTABLISHED   9372   chrome.exe
tcp   192.168.1.101:53809            151.101.0.133:443              ESTABLISHED   9372   chrome.exe
tcp   192.168.1.101:53836            151.101.0.133:443              ESTABLISHED   9372   chrome.exe
tcp   192.168.1.101:53812            151.101.0.133:443              ESTABLISHED   9372   chrome.exe
tcp   127.0.0.1:50151                127.0.0.1:50152                ESTABLISHED   6596   eclipse.exe
tcp   192.168.1.101:53827            192.30.253.112:443             CLOSE_WAIT    9372   chrome.exe
tcp   192.168.1.101:53806            151.101.0.133:443              ESTABLISHED   9372   chrome.exe
tcp   192.168.1.101:53802            192.30.253.117:443             CLOSE_WAIT    9372   chrome.exe
udp   192.168.1.101:138              -                              NONE          4      System
tcp   0.0.0.0:3306                   -                              LISTEN        3644   mysqld.exe
tcp   192.168.1.101:53831            151.101.0.133:443              ESTABLISHED   9372   chrome.exe
tcp6  :::50154                       -                              LISTEN        6596   eclipse.exe
udp   192.168.1.101:59576            -                              NONE          4764   UoipService.exe
'''
    
    
# print(psutil.net_if_addrs()) # many more: {'Local Area Connection* 2': [snic(family=<AddressFamily.AF_LINK: -1>, address='78-0C-B8-B1-51-FD', netmask=None, broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET: 2>, address='169.254.168.109', netmask='255.255.0.0', broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET6: 23>, address='fe80::6542:b6b9:5895:a86d', netmask=None, broadcast=None, ptp=None)], 'Wi-Fi': [snic(family=<AddressFamily.AF_LINK: -1>, address='78-0C-B8-B1-51-FC', netmask=None, broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET: 2>, address='192.168.1.101', netmask='255.255.255.0', broadcast=None, ptp=None), snic(family=<AddressFamily.A



# for proc in psutil.process_iter():
#     try:
#         pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
#     except psutil.NoSuchProcess:
#         pass
#     else:
#         print(pinfo)

''' many more
{'username': 'NT AUTHORITY\\SYSTEM', 'pid': 0, 'name': 'System Idle Process'}
{'username': 'NT AUTHORITY\\SYSTEM', 'pid': 4, 'name': 'System'}
{'username': None, 'pid': 8, 'name': 'fontdrvhost.exe'}
{'username': None, 'pid': 76, 'name': 'svchost.exe'}
{'username': None, 'pid': 300, 'name': 'svchost.exe'}
{'username': None, 'pid': 372, 'name': 'WUDFHost.exe'}
{'username': None, 'pid': 384, 'name': 'svchost.exe'}
{'username': None, 'pid': 408, 'name': 'smss.exe'}
{'username': 'BURKHARD-DELL\\Burkh', 'pid': 496, 'name': 'chrome.exe'}
'''

# more compact code same results as above
# for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
#     print(proc.info)


# procs = {p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username'])}
# print(procs)
# {0: {'name': 'System Idle Process', 'username': 'NT AUTHORITY\\SYSTEM'}, 4: {'name': 'System', 'username': 'NT AUTHORITY\\SYSTEM'},


# print([p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'python' in p.info['name']])
# [{'name': 'python.exe', 'pid': 4992}, {'name': 'python.exe', 'pid': 5596}, {'name': 'python.exe', 'pid': 12280}]


# for p in psutil.process_iter(attrs=['name', 'open_files']):
#     for file in p.info['open_files'] or []:
#         if os.path.splitext(file.path)[1] == '.log':
#             print("%-5s %-10s %s" % (p.pid, p.info['name'][:10], file.path))


# and more processes that create log files
# 6596  eclipse.ex C:\Eclipse_Oxygen_workspace_Packt\.metadata\.plugins\org.eclipse.m2e.logback.configuration\0.log
# 7924  taskhostw. C:\Users\Burkh\AppData\Local\Microsoft\Windows\WebCache\V01.log





p = psutil.Process()
# print(p.memory_info())
# pmem(rss=14544896, vms=8163328, num_page_faults=6820, peak_wset=14987264, wset=14544896, peak_paged_pool=203000, paged_pool=202776, peak_nonpaged_pool=13440, nonpaged_pool=13168, pagefile=8163328, peak_pagefile=8519680, private=8163328)

# print(p.memory_full_info())
# pfullmem(rss=14880768, vms=8491008, num_page_faults=6821, peak_wset=14987264, wset=14880768, peak_paged_pool=203000, paged_pool=202776, peak_nonpaged_pool=13440, nonpaged_pool=13168, pagefile=8491008, peak_pagefile=8495104, private=8491008, uss=7409664)

# print(list(psutil.win_service_iter()))
# [<WindowsService(name='AdobeARMservice', display_name='Adobe Acrobat Update Service') at 1922689993080>, <WindowsService(name='AJRouter', display_name='AllJoyn Router Service') at 1922689993136>, <WindowsService(name='ALG', display_name='Application Layer Gateway Service') at 1922689993192>, <WindowsService(name='AppIDSvc', display_name='Application Identity') at 1922689993248>, <WindowsService(name='Appinfo', display_name='Application Information') at 1922689993304>, <WindowsService(name='AppReadiness', display_name='App Readiness') at 1922689993360>, <WindowsService(name='AppXSvc', display_name='AppX Deployment Service (AppXSVC)') at 1922689993416>, <WindowsService(name='AudioEndpointBuilder', display_name='Windows Audio Endpoint Builder') at 1922689993472>, <WindowsService(name='Audiosrv', display_name='Windows Audio') at 1922689993528>, <WindowsService(name='AxInstSV', display_name='ActiveX Installer (AxInstSV)') at 1922689993584>, <WindowsService(name='BDESVC', display_name='BitLocker Drive Encryption Service') at 1922689993640>, <WindowsService(name='BFE', display_name='Base Filtering Engine') at 1922689993696>, <WindowsService(name='BITS', display_name='Background Intelligent Transfer Service') at 1922689993752>, <WindowsService(name='BrokerInfrastructure', display_name='Background Tasks Infrastructure Service') at 1922689993808>, <WindowsService(name='BthHFSrv', display_name='Bluetooth Handsfree Service') at 1922689993864>, <WindowsService(name='bthserv', display_name='Bluetooth Support Service') at 1922689993920>, <WindowsService(name='camsvc', display_name='Capability Access Manager Service') at 1922689993976>, <WindowsService(name='CDPSvc', display_name='Connected Devices Platform Service') at 1922689994032>, <WindowsService(name='CertPropSvc', display_name='Certificate Propagation') at 1922689994088>, <WindowsService(name='ClickToRunSvc', display_name='Microsoft Office ClickToRun Service') at 1922689994144>, <WindowsService(name='ClientAnalyticsService', display_name='ClientAnalyticsService') at 1922689994200>, <WindowsService(name='ClipSVC', display_name='Client License Service (ClipSVC)') at 1922689994256>, <WindowsService(name='COMSysApp', display_name='COM+ System Application') at 1922689994312>, <WindowsService(name='CoreMessagingRegistrar', display_name='CoreMessaging') at 1922689994368>, <WindowsService(name='cphs', display_name='Intel(R) Content Protection HECI Service') at 1922689994424>, <WindowsService(name='CryptSvc', display_name='Cryptographic Services') at 1922689994480>, <WindowsService(name='DcomLaunch', display_name='DCOM Server Process Launcher') at 1922689994536>, <WindowsService(name='defragsvc', display_name='Optimize drives') at 1922689994592>, <WindowsService(name='Dell Customer Connect', display_name='Dell Customer Connect') at 1922689994648>, <WindowsService(name='Dell Help & Support', display_name='Dell Help & Support') at 1922689994704>, <WindowsService(name='DellDigitalDelivery', display_name='Dell Digital Delivery Service') at 1922690019400>, <WindowsService(name='DellUpdate', display_name='Dell Update Service') at 1922690019456>, <WindowsService(name='DeviceAssociationService', display_name='Device Association Service') at 1922690019512>, <WindowsService(name='DeviceInstall', display_name='Device Install Service') at 1922690019568>, <WindowsService(name='DevQueryBroker', display_name='DevQuery Background Discovery Broker') at 1922690019624>, <WindowsService(name='Dhcp', display_name='DHCP Client') at 1922690019680>, <WindowsService(name='diagnosticshub.standardcollector.service', display_name='Microsoft (R) Diagnostics Hub Standard Collector Service') at 1922690019736>, <WindowsService(name='diagsvc', display_name='Diagnostic Execution Service') at 1922690019792>, <WindowsService(name='DiagTrack', display_name='Connected User Experiences and Telemetry') at 1922690019848>, <WindowsService(name='DmEnrollmentSvc', display_name='Device Management Enrollment Service') at 1922690019904>, <WindowsService(name='dmwappushservice', display_name='dmwappushsvc') at 1922690019960>, <WindowsService(name='Dnscache', display_name='DNS Client') at 1922690020016>, <WindowsService(name='DoSvc', display_name='Delivery Optimization') at 1922690020072>, <WindowsService(name='dot3svc', display_name='Wired AutoConfig') at 1922690020128>, <WindowsService(name='DPS', display_name='Diagnostic Policy Service') at 1922690020184>, <WindowsService(name='DsmSvc', display_name='Device Setup Manager') at 1922690020240>, <WindowsService(name='DsSvc', display_name='Data Sharing Service') at 1922690020296>, <WindowsService(name='DusmSvc', display_name='Data Usage') at 1922690020352>, <WindowsService(name='Eaphost', display_name='Extensible Authentication Protocol') at 1922690020408>, <WindowsService(name='EFS', display_name='Encrypting File System (EFS)') at 1922690020464>, <WindowsService(name='embeddedmode', display_name='Embedded Mode') at 1922690020520>, <WindowsService(name='EntAppSvc', display_name='Enterprise App Management Service') at 1922690020576>, <WindowsService(name='esifsvc', display_name='ESIF Upper Framework Service') at 1922690020632>, <WindowsService(name='EventLog', display_name='Windows Event Log') at 1922690020688>, <WindowsService(name='EventSystem', display_name='COM+ Event System') at 1922690020744>, <WindowsService(name='EvtEng', display_name='Intel(R) PROSet/Wireless Event Log') at 1922690020800>, <WindowsService(name='Fax', display_name='Fax') at 1922690020856>, <WindowsService(name='fdPHost', display_name='Function Discovery Provider Host') at 1922690020912>, <WindowsService(name='FDResPub', display_name='Function Discovery Resource Publication') at 1922690020968>, <WindowsService(name='fhsvc', display_name='File History Service') at 1922690021024>, <WindowsService(name='FontCache', display_name='Windows Font Cache Service') at 1922690021080>, <WindowsService(name='FontCache3.0.0.0', display_name='Windows Presentation Foundation Font Cache 3.0.0.0') at 1922690021136>, <WindowsService(name='FrameServer', display_name='Windows Camera Frame Server') at 1922690021192>, <WindowsService(name='fussvc', display_name='Windows App Certification Kit Fast User Switching Utility Service') at 1922690021248>, <WindowsService(name='gpsvc', display_name='Group Policy Client') at 1922690021304>, <WindowsService(name='GraphicsPerfSvc', display_name='GraphicsPerfSvc') at 1922690021360>, <WindowsService(name='gupdate', display_name='Google Update Service (gupdate)') at 1922690021416>, <WindowsService(name='gupdatem', display_name='Google Update Service (gupdatem)') at 1922690021472>, <WindowsService(name='hidserv', display_name='Human Interface Device Service') at 1922690021528>, <WindowsService(name='HomeGroupProvider', display_name='HomeGroup Provider') at 1922690021584>, <WindowsService(name='HvHost', display_name='HV Host Service') at 1922690021640>, <WindowsService(name='IAStorDataMgrSvc', display_name='Intel(R) Rapid Storage Technology') at 1922690021696>, <WindowsService(name='ibtsiva', display_name='Intel Bluetooth Service') at 1922690021752>, <WindowsService(name='icssvc', display_name='Windows Mobile Hotspot Service') at 1922690021808>, <WindowsService(name='igfxCUIService2.0.0.0', display_name='Intel(R) HD Graphics Control Panel Service') at 1922690021864>, <WindowsService(name='IKEEXT', display_name='IKE and AuthIP IPsec Keying Modules') at 1922690021920>, <WindowsService(name='InstallService', display_name='Windows Store Install Service') at 1922690021976>, <WindowsService(name='Intel(R) WiDi SAM', display_name='Intel(R) WiDi Software Asset Manager') at 1922690022032>, <WindowsService(name='IntelUSBoverIP', display_name='IntelUSBoverIP') at 1922690022088>, <WindowsService(name='iphlpsvc', display_name='IP Helper') at 1922690022144>, <WindowsService(name='IpxlatCfgSvc', display_name='IP Translation Configuration Service') at 1922690022200>, <WindowsService(name='irmon', display_name='Infrared monitor service') at 1922690022256>, <WindowsService(name='KeyIso', display_name='CNG Key Isolation') at 1922690022312>, <WindowsService(name='KtmRm', display_name='KtmRm for Distributed Transaction Coordinator') at 1922690022368>, <WindowsService(name='LanmanServer', display_name='Server') at 1922690022424>, <WindowsService(name='LanmanWorkstation', display_name='Workstation') at 1922690022480>, <WindowsService(name='lfsvc', display_name='Geolocation Service') at 1922690022536>, <WindowsService(name='LicenseManager', display_name='Windows License Manager Service') at 1922690022592>, <WindowsService(name='lltdsvc', display_name='Link-Layer Topology Discovery Mapper') at 1922690022648>, <WindowsService(name='lmhosts', display_name='TCP/IP NetBIOS Helper') at 1922690022704>, <WindowsService(name='LSM', display_name='Local Session Manager') at 1922690022760>, <WindowsService(name='MapsBroker', display_name='Downloaded Maps Manager') at 1922690022816>, <WindowsService(name='McAfee SiteAdvisor Service', display_name='McAfee SiteAdvisor Service') at 1922690022872>, <WindowsService(name='McAPExe', display_name='McAfee AP Service') at 1922690022928>, <WindowsService(name='mccspsvc', display_name='McAfee CSP Service') at 1922690022984>, <WindowsService(name='mfefire', display_name='McAfee Firewall Core Service') at 1922690023040>, <WindowsService(name='mfemms', display_name='McAfee Service Controller') at 1922690023096>, <WindowsService(name='mfevtp', display_name='McAfee Validation Trust Protection Service') at 1922690023152>, <WindowsService(name='ModuleCoreService', display_name='McAfee Module Core Service') at 1922690023208>, <WindowsService(name='MpsSvc', display_name='Windows Defender Firewall') at 1922690023264>, <WindowsService(name='MSDTC', display_name='Distributed Transaction Coordinator') at 1922690023320>, <WindowsService(name='MSiSCSI', display_name='Microsoft iSCSI Initiator Service') at 1922690023376>, <WindowsService(name='msiserver', display_name='Windows Installer') at 1922690035784>, <WindowsService(name='MySQL57', display_name='MySQL57') at 1922690035840>, <WindowsService(name='MyWiFiDHCPDNS', display_name='Wireless PAN DHCP Server') at 1922690035896>, <WindowsService(name='NaturalAuthentication', display_name='Natural Authentication') at 1922690035952>, <WindowsService(name='NcaSvc', display_name='Network Connectivity Assistant') at 1922690036008>, <WindowsService(name='NcbService', display_name='Network Connection Broker') at 1922690036064>, <WindowsService(name='NcdAutoSetup', display_name='Network Connected Devices Auto-Setup') at 1922690036120>, <WindowsService(name='Net Driver HPZ12', display_name='Net Driver HPZ12') at 1922690036176>, <WindowsService(name='Netlogon', display_name='Netlogon') at 1922690036232>, <WindowsService(name='Netman', display_name='Network Connections') at 1922690036288>, <WindowsService(name='netprofm', display_name='Network List Service') at 1922690036344>, <WindowsService(name='NetSetupSvc', display_name='Network Setup Service') at 1922690036400>, <WindowsService(name='NetTcpPortSharing', display_name='Net.Tcp Port Sharing Service') at 1922690036456>, <WindowsService(name='NgcCtnrSvc', display_name='Microsoft Passport Container') at 1922690036512>, <WindowsService(name='NgcSvc', display_name='Microsoft Passport') at 1922690036568>, <WindowsService(name='NlaSvc', display_name='Network Location Awareness') at 1922690036624>, <WindowsService(name='nsi', display_name='Network Store Interface Service') at 1922690036680>, <WindowsService(name='ose64', display_name='Office 64 Source Engine') at 1922690036736>, <WindowsService(name='p2pimsvc', display_name='Peer Networking Identity Manager') at 1922690036792>, <WindowsService(name='p2psvc', display_name='Peer Networking Grouping') at 1922690036848>, <WindowsService(name='PanoptoRecorderService', display_name='Panopto Upload Service') at 1922690036904>, <WindowsService(name='PcaSvc', display_name='Program Compatibility Assistant Service') at 1922690036960>, <WindowsService(name='PEFService', display_name='McAfee PEF Service') at 1922690037016>, <WindowsService(name='PerfHost', display_name='Performance Counter DLL Host') at 1922690037072>, <WindowsService(name='PhoneSvc', display_name='Phone Service') at 1922690037128>, <WindowsService(name='pla', display_name='Performance Logs & Alerts') at 1922690037184>, <WindowsService(name='PlugPlay', display_name='Plug and Play') at 1922690037240>, <WindowsService(name='Pml Driver HPZ12', display_name='Pml Driver HPZ12') at 1922690037296>, <WindowsService(name='PNRPAutoReg', display_name='PNRP Machine Name Publication Service') at 1922690037352>, <WindowsService(name='PNRPsvc', display_name='Peer Name Resolution Protocol') at 1922690037408>, <WindowsService(name='PolicyAgent', display_name='IPsec Policy Agent') at 1922690037464>, <WindowsService(name='Power', display_name='Power') at 1922690037520>, <WindowsService(name='PrintNotify', display_name='Printer Extensions and Notifications') at 1922690037576>, <WindowsService(name='Product Registration', display_name='Product Registration') at 1922690037632>, <WindowsService(name='ProfSvc', display_name='User Profile Service') at 1922690037688>, <WindowsService(name='PushToInstall', display_name='Windows PushToInstall Service') at 1922690037744>, <WindowsService(name='PythonTaskSvc', display_name='Python Task Scheduling Service') at 1922690037800>, <WindowsService(name='QWAVE', display_name='Quality Windows Audio Video Experience') at 1922690037856>, <WindowsService(name='RasAuto', display_name='Remote Access Auto Connection Manager') at 1922690037912>, <WindowsService(name='RasMan', display_name='Remote Access Connection Manager') at 1922690037968>, <WindowsService(name='RegSrvc', display_name='Intel(R) PROSet/Wireless Registry Service') at 1922690038024>, <WindowsService(name='RemoteAccess', display_name='Routing and Remote Access') at 1922690038080>, <WindowsService(name='RemoteRegistry', display_name='Remote Registry') at 1922690038136>, <WindowsService(name='RetailDemo', display_name='Retail Demo Service') at 1922690038192>, <WindowsService(name='RmSvc', display_name='Radio Management Service') at 1922690038248>, <WindowsService(name='RpcEptMapper', display_name='RPC Endpoint Mapper') at 1922690038304>, <WindowsService(name='RpcLocator', display_name='Remote Procedure Call (RPC) Locator') at 1922690038360>, <WindowsService(name='RpcSs', display_name='Remote Procedure Call (RPC)') at 1922690038416>, <WindowsService(name='RtkAudioService', display_name='Realtek Audio Service') at 1922690038472>, <WindowsService(name='SamSs', display_name='Security Accounts Manager') at 1922690038528>, <WindowsService(name='SCardSvr', display_name='Smart Card') at 1922690038584>, <WindowsService(name='ScDeviceEnum', display_name='Smart Card Device Enumeration Service') at 1922690038640>, <WindowsService(name='Schedule', display_name='Task Scheduler') at 1922690038696>, <WindowsService(name='SCPolicySvc', display_name='Smart Card Removal Policy') at 1922690038752>, <WindowsService(name='SDRSVC', display_name='Windows Backup') at 1922690038808>, <WindowsService(name='seclogon', display_name='Secondary Logon') at 1922690038864>, <WindowsService(name='SecurityHealthService', display_name='Windows Defender Security Center Service') at 1922690038920>, <WindowsService(name='SEMgrSvc', display_name='Payments and NFC/SE Manager') at 1922690038976>, <WindowsService(name='SENS', display_name='System Event Notification Service') at 1922690039032>, <WindowsService(name='SensorDataService', display_name='Sensor Data Service') at 1922690039088>, <WindowsService(name='SensorService', display_name='Sensor Service') at 1922690039144>, <WindowsService(name='SensrSvc', display_name='Sensor Monitoring Service') at 1922690039200>, <WindowsService(name='SessionEnv', display_name='Remote Desktop Configuration') at 1922690039256>, <WindowsService(name='SharedAccess', display_name='Internet Connection Sharing (ICS)') at 1922690039312>, <WindowsService(name='SharedRealitySvc', display_name='Spatial Data Service') at 1922690039368>, <WindowsService(name='ShellHWDetection', display_name='Shell Hardware Detection') at 1922690039424>, <WindowsService(name='shpamsvc', display_name='Shared PC Account Manager') at 1922690039480>, <WindowsService(name='SkypeUpdate', display_name='Skype Updater') at 1922690039536>, <WindowsService(name='smphost', display_name='Microsoft Storage Spaces SMP') at 1922690039592>, <WindowsService(name='SmsRouter', display_name='Microsoft Windows SMS Router Service.') at 1922690039648>, <WindowsService(name='SNMPTRAP', display_name='SNMP Trap') at 1922690039704>, <WindowsService(name='spectrum', display_name='Windows Perception Service') at 1922690039760>, <WindowsService(name='Spooler', display_name='Print Spooler') at 1922690048072>, <WindowsService(name='sppsvc', display_name='Software Protection') at 1922690048128>, <WindowsService(name='SSDPSRV', display_name='SSDP Discovery') at 1922690048184>, <WindowsService(name='SstpSvc', display_name='Secure Socket Tunneling Protocol Service') at 1922690048240>, <WindowsService(name='StateRepository', display_name='State Repository Service') at 1922690048296>, <WindowsService(name='stisvc', display_name='Windows Image Acquisition (WIA)') at 1922690048352>, <WindowsService(name='StorSvc', display_name='Storage Service') at 1922690048408>, <WindowsService(name='svsvc', display_name='Spot Verifier') at 1922690048464>, <WindowsService(name='swprv', display_name='Microsoft Software Shadow Copy Provider') at 1922690048520>, <WindowsService(name='SysMain', display_name='Superfetch') at 1922690048576>, <WindowsService(name='SystemEventsBroker', display_name='System Events Broker') at 1922690048632>, <WindowsService(name='TabletInputService', display_name='Touch Keyboard and Handwriting Panel Service') at 1922690048688>, <WindowsService(name='TapiSrv', display_name='Telephony') at 1922690048744>, <WindowsService(name='Te.Service', display_name='Te.Service') at 1922690048800>, <WindowsService(name='TermService', display_name='Remote Desktop Services') at 1922690048856>, <WindowsService(name='Themes', display_name='Themes') at 1922690048912>, <WindowsService(name='TieringEngineService', display_name='Storage Tiers Management') at 1922690048968>, <WindowsService(name='tiledatamodelsvc', display_name='Tile Data model server') at 1922690049024>, <WindowsService(name='TimeBrokerSvc', display_name='Time Broker') at 1922690049080>, <WindowsService(name='TokenBroker', display_name='Web Account Manager') at 1922690049136>, <WindowsService(name='TrkWks', display_name='Distributed Link Tracking Client') at 1922690049192>, <WindowsService(name='TrustedInstaller', display_name='Windows Modules Installer') at 1922690049248>, <WindowsService(name='tzautoupdate', display_name='Auto Time Zone Updater') at 1922690049304>, <WindowsService(name='UI0Detect', display_name='Interactive Services Detection') at 1922690049360>, <WindowsService(name='UmRdpService', display_name='Remote Desktop Services UserMode Port Redirector') at 1922690049416>, <WindowsService(name='upnphost', display_name='UPnP Device Host') at 1922690049472>, <WindowsService(name='UserManager', display_name='User Manager') at 1922690049528>, <WindowsService(name='UsoSvc', display_name='Update Orchestrator Service') at 1922690049584>, <WindowsService(name='VaultSvc', display_name='Credential Manager') at 1922690049640>, <WindowsService(name='vds', display_name='Virtual Disk') at 1922690049696>, <WindowsService(name='vmicguestinterface', display_name='Hyper-V Guest Service Interface') at 1922690049752>, <WindowsService(name='vmicheartbeat', display_name='Hyper-V Heartbeat Service') at 1922690049808>, <WindowsService(name='vmickvpexchange', display_name='Hyper-V Data Exchange Service') at 1922690049864>, <WindowsService(name='vmicrdv', display_name='Hyper-V Remote Desktop Virtualization Service') at 1922690049920>, <WindowsService(name='vmicshutdown', display_name='Hyper-V Guest Shutdown Service') at 1922690049976>, <WindowsService(name='vmictimesync', display_name='Hyper-V Time Synchronization Service') at 1922690050032>, <WindowsService(name='vmicvmsession', display_name='Hyper-V PowerShell Direct Service') at 1922690050088>, <WindowsService(name='vmicvss', display_name='Hyper-V Volume Shadow Copy Requestor') at 1922690050144>, <WindowsService(name='VSS', display_name='Volume Shadow Copy') at 1922690050200>, <WindowsService(name='W32Time', display_name='Windows Time') at 1922690050256>, <WindowsService(name='WalletService', display_name='WalletService') at 1922690050312>, <WindowsService(name='WarpJITSvc', display_name='WarpJITSvc') at 1922690050368>, <WindowsService(name='WavesSysSvc', display_name='Waves System Service') at 1922690050424>, <WindowsService(name='wbengine', display_name='Block Level Backup Engine Service') at 1922690050480>, <WindowsService(name='WbioSrvc', display_name='Windows Biometric Service') at 1922690050536>, <WindowsService(name='Wcmsvc', display_name='Windows Connection Manager') at 1922690050592>, <WindowsService(name='wcncsvc', display_name='Windows Connect Now - Config Registrar') at 1922690050648>, <WindowsService(name='WdiServiceHost', display_name='Diagnostic Service Host') at 1922690050704>, <WindowsService(name='WdiSystemHost', display_name='Diagnostic System Host') at 1922690050760>, <WindowsService(name='WdNisSvc', display_name='Windows Defender Antivirus Network Inspection Service') at 1922690050816>, <WindowsService(name='WebClient', display_name='WebClient') at 1922690050872>, <WindowsService(name='Wecsvc', display_name='Windows Event Collector') at 1922690050928>, <WindowsService(name='WEPHOSTSVC', display_name='Windows Encryption Provider Host Service') at 1922690050984>, <WindowsService(name='wercplsupport', display_name='Problem Reports and Solutions Control Panel Support') at 1922690051040>, <WindowsService(name='WerSvc', display_name='Windows Error Reporting Service') at 1922690051096>, <WindowsService(name='WFDSConMgrSvc', display_name='Wi-Fi Direct Services Connection Manager Service') at 1922690051152>, <WindowsService(name='WiaRpc', display_name='Still Image Acquisition Events') at 1922690051208>, <WindowsService(name='WinDefend', display_name='Windows Defender Antivirus Service') at 1922690051264>, <WindowsService(name='WinHttpAutoProxySvc', display_name='WinHTTP Web Proxy Auto-Discovery Service') at 1922690051320>, <WindowsService(name='Winmgmt', display_name='Windows Management Instrumentation') at 1922690051376>, <WindowsService(name='WinRM', display_name='Windows Remote Management (WS-Management)') at 1922690051432>, <WindowsService(name='wisvc', display_name='Windows Insider Service') at 1922690051488>, <WindowsService(name='WlanSvc', display_name='WLAN AutoConfig') at 1922690051544>, <WindowsService(name='wlidsvc', display_name='Microsoft Account Sign-in Assistant') at 1922690051600>, <WindowsService(name='wlpasvc', display_name='Local Profile Assistant Service') at 1922690051656>, <WindowsService(name='wmiApSrv', display_name='WMI Performance Adapter') at 1922690051712>, <WindowsService(name='WMPNetworkSvc', display_name='Windows Media Player Network Sharing Service') at 1922690051768>, <WindowsService(name='workfolderssvc', display_name='Work Folders') at 1922690051824>, <WindowsService(name='WPDBusEnum', display_name='Portable Device Enumerator Service') at 1922690051880>, <WindowsService(name='WpnService', display_name='Windows Push Notifications System Service') at 1922690051936>, <WindowsService(name='wscsvc', display_name='Security Center') at 1922690051992>, <WindowsService(name='WSearch', display_name='Windows Search') at 1922690052048>, <WindowsService(name='wuauserv', display_name='Windows Update') at 1922690060360>, <WindowsService(name='WwanSvc', display_name='WWAN AutoConfig') at 1922690060416>, <WindowsService(name='xbgm', display_name='Xbox Game Monitoring') at 1922690060472>, <WindowsService(name='XblAuthManager', display_name='Xbox Live Auth Manager') at 1922690060528>, <WindowsService(name='XblGameSave', display_name='Xbox Live Game Save') at 1922690060584>, <WindowsService(name='XboxGipSvc', display_name='Xbox Accessory Management Service') at 1922690060640>, <WindowsService(name='XboxNetApiSvc', display_name='Xbox Live Networking Service') at 1922690060696>, <WindowsService(name='ZeroConfigService', display_name='Intel(R) PROSet/Wireless Zero Configuration Service') at 1922690060752>, <WindowsService(name='CDPUserSvc_5c82d', display_name='CDPUserSvc_5c82d') at 1922690060808>, <WindowsService(name='DevicesFlowUserSvc_5c82d', display_name='DevicesFlowUserSvc_5c82d') at 1922690060864>, <WindowsService(name='MessagingService_5c82d', display_name='MessagingService_5c82d') at 1922690060920>, <WindowsService(name='OneSyncSvc_5c82d', display_name='OneSyncSvc_5c82d') at 1922690060976>, <WindowsService(name='PimIndexMaintenanceSvc_5c82d', display_name='PimIndexMaintenanceSvc_5c82d') at 1922690061032>, <WindowsService(name='PrintWorkflowUserSvc_5c82d', display_name='PrintWorkflowUserSvc_5c82d') at 1922690061088>, <WindowsService(name='UnistoreSvc_5c82d', display_name='UnistoreSvc_5c82d') at 1922690061144>, <WindowsService(name='UserDataSvc_5c82d', display_name='UserDataSvc_5c82d') at 1922690061200>, <WindowsService(name='WpnUserService_5c82d', display_name='WpnUserService_5c82d') at 1922690061256>]















    
    
    
    
    
    
    
    