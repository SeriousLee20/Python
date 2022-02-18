import time
import os
#t = (2015,12,31,10,39,45,1,48,0)
#t = time.mktime(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.localtime()))

print(time.strptime("Monday 29 Jun 2020 20:30:27", "%A %d %b %Y %H:%M:%S"))



os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print( time.strftime('%X %x %Z'))
 
os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print (time.strftime('%X %x %Z'))