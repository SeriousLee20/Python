dict = {'Name' : 'Manni', 'Age' : 7, 'Class' : 'First'}

print(dict)
print(type(dict))

#o/p the str representation of the dict
print(str(dict))

#Length of dict
print("Length : %d" %len(dict))

#dict.copy() can return value
print(dict.copy())

#dict.get()
print(dict.get('Name',"NA"))
print(dict.get('Sex'))

#dict.items() o/p style
print("Value1: " + str(dict.items()))
print("Value2: " , dict.items())
print("Value3: %s" % dict.items())
items = dict.items() 
print(items)

#dict.values o/p as seq
print(dict.values())
#change the dict into list
print(list(dict.keys()))

print(dict.setdefault('Sex','F'))
print(dict)
