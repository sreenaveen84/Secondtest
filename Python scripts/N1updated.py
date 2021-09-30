import re

# original string with unwanted chars
originalString = "m$%y &nam12e is A^le%x"

# printing original string
print ("Original String : ", originalString)

required_string = re.sub(r"[^a-zA-Z.\s]",'',originalString)

print ("Required string is : ", str(required_string))