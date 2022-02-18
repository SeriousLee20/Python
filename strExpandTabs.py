s='\t\t'
print(len(s)) #the len() count 2 tabs
print(len(s.expandtabs())) #len() counts 16 spaces
print(len(s.expandtabs(16))) #len() counts 32 spaces

s='\t'
print(len(s)) #len() counts 1 tab
print(len(s.expandtabs())) #len() counts 8 spaces
print(len(s.expandtabs(16))) #len() counts 16 spaces

s='abc\tabc'
print(len(s)) #len() counts 6 letters + 1 tab
print(s)
          
#simply assume 8 spaces + 3 letters after \t; 
#8-3=5,start the spaces at index 4 
print(len(s.expandtabs()))
print(s.expandtabs())

#simply assume 16 spaces + 3 letters after \t
#16-3=13spaces, spaces start at index 4
print(len(s.expandtabs(16)))
print(s.expandtabs(16))

s='abc\t\tabc'
print(len(s)) #6 letters +2 tabs
print(s)

#simply assume 16 spaces + 3 char after \t
#8-3=5, 5+8=13 spaces, spaces start at the index 4
print(len(s.expandtabs()))
print(s.expandtabs())

#simply assumes 32 spaces + 3 chars after \t
#16-3=13, 13+16=29, spaces start at index 4
print(len(s.expandtabs(16)))
print(s.expandtabs(16))
