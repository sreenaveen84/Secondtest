import re
#string = "Altiostar_VCU_123"
string = "_Altiostar_13_VCU_123_"

print("Input:", string) #printing original string

e = string.split('_')
#print("Separated list:",e)

while("" in e):
    e.remove("")
    #print(e)

s = "-".join([i for i in e if not i.isdigit()])
f = str.lower(s)
print("Output:", f)