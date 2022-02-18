sampleList = [87, 45, 41, 65, 94, 41, 99, 93]
list(set(sampleList))

print("unique items",list(dict.fromkeys(sampleList)))

print("tuple",tuple(dict.fromkeys(sampleList)))
        
       
print("Min: %s" % min(sampleList) ,"Max:%s" %max(sampleList))