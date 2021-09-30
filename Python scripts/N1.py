 
unwantedChars = ['$', '%', '&', '^', '1', '2']

# original string with unwanted chars
originalString = "m$%y &nam12e is A^le%x"

# printing original string
print ("Original String : ", originalString)
print(type(originalString))

# using replace() to remove unwanted chars in a string
for a in unwantedChars :
	originalString = originalString.replace(a, '')

# print required string
print ("Required string is : ", str(originalString))