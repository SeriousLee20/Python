import time
print(time.time())
print()
print(time.localtime())
print()

print(time.asctime())
print(time.asctime(time.localtime()))
print(time.asctime(time.gmtime()))
print(time.ctime())


print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.mktime(time.localtime()))
print(time.gmtime())
print()
print(time.gmtime(time.time()))