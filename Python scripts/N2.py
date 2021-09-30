string = "Altiostar_VCU_123"

print("Input:", string) #printing original string

string = string.replace('_', '-')

print("Output:", string.lower()[0:-4]) #printing only required lenghth with lowercase letters