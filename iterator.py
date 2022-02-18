list=[1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator

for x in it:
    print (x, end=" ")

import sys
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()