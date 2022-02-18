str = 'this is\tstring example'

print(str.center(40,'i'))

print(str.count('exam',10,40))

#isnumeric() method
s='一二三四'
print(s.isnumeric())

#expandtabs() method, extra in another file
str = 'this is\tstring example....wow!!!!'
print(str)
print(str.expandtabs())
print(str.expandtabs(16))

#split() method: if the char is provided,
#the char is the point to be splitted, not printed
print(str.split('s',3))

#splines() method: diff o/p
str = 'this is\nstring e\nxample....\nwow!!!!'
print(str.splitlines())
print(str.splitlines(0))
print(str.splitlines(1))
print(str.splitlines(True))

x=input("Number: ")
print(x.isspace())
if x.isspace():
    print("Enter a number: ")
    x=str(input("Number: "))