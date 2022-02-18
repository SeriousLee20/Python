#input("Sentence: ")
isUpper=0
isLower=0
isSpecial=0
isDigit=0
for char in input("Sentence:"):
    if(char.isupper()):
        isUpper+=1
    elif(char.islower()):
        isLower+=1
    elif(char.isdigit()):
        isDigit+=1
    elif(not char.isalnum() and not char.isspace() ):
        isSpecial+=1
        
print("UpperCase:", isUpper, ", LowerCase:", isLower, ", Digit: ",isDigit, ", SpecialChar: ", isSpecial)