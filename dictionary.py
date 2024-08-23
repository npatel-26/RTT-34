# Create a dictionary and create four key:valuepairs in it
myDict= {}
myDict["one"] = 1
myDict["two"] = 2
myDict[3] = "three"
myDict["four"] = 4.4

#Print the third value in your dictionary
print(myDict[3])

#Print your entire dictionary.
for key, value in myDict.items():
    print(key, value)
