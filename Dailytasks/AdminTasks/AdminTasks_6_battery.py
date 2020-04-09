import psutil                      

print('BATTERY Related ----')
def from_seconds(seconds):
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

battery = psutil.sensors_battery()
print(battery)
print('Battery charge= {}%, Battery time left= {}'.format(battery.percent, from_seconds(battery.secsleft)))


















