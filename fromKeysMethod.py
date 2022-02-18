
seq = ('name', 'age', 'sex')

#create a dict without values
dict = dict.fromkeys(seq)
print ("New Dictionary : %s" % str(dict))

#assign the keys with value 10
dict = dict.fromkeys(seq, 10)
print ("New Dictionary : %s" % str(dict))

lis1 = [2,3]

#assign the keys with a list of seq
#using conventional way
#dict = dict.fromkeys(seq,lis1) **if o/p directly
print(dict.fromkeys(seq,lis1))

#append the list with 4
lis1.append(4)
#the values of the dict is updated
print(dict.fromkeys(seq,lis1))

lis1 = [2,3]
#using fromkeys() to convert a seq to dict
dict = {key : list(lis1) for key in seq}
print(dict)

lis1.append(4)
#the values of the dict are unchanged
print(dict)