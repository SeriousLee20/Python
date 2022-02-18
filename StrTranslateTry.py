#from string import maketrans # Required to call maketrans function.
intab = "aeiouxm"
outtab = "1234512"
trantab =str.maketrans(intab, outtab,"xm")
str = "this is string example....wow!!!";
print (str.translate(trantab))