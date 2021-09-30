import re
class StringFormatter:

    def __init__(self , CustomerInput, CustomerString):
        self.CustomerInput = CustomerInput
        self.CustomerString = CustomerString
        if self.CustomerInput == 1:
           StringFormatter.remove_unwanted_text(self);
        elif self.CustomerInput == 2:
            StringFormatter.remove_numeric_values(self);
        elif self.CustomerInput == 3:
            StringFormatter.replace_string_with_required_string(self);
        else:
            print("\nU-oh, Enter 1 or 2 or 3 only")
        
    def remove_unwanted_text(self):
        #original string with unwanted chars
        #originalString = "m$%y &nam12e is A^le%x"
        
        print ("Original String : ", self.CustomerString) # printing original string

        required_string = re.sub(r"[^a-zA-Z.\s]",'',self.CustomerString)

        print ("Required string is : ", str(required_string))
        
    def remove_numeric_values(self):
        #string = "Altiostar_VCU_123"
        #string = "_Altiostar_13_VCU_123_"
        
        print("Input:", self.CustomerString) #printing original string

        e = self.CustomerString.split('_')
        
        while("" in e):
            e.remove("")
            #print(e)

        s = "-".join([i for i in e if not i.isdigit()])
        f = str.lower(s)
        print("Output:", f)
        
    def replace_string_with_required_string(self):
        #string = "Altiostar vcu and vdu deployment on openstack"
        
        print("Input:", self.CustomerString) #printing original string

        string = self.CustomerString.replace('openstack', 'Azure')

        print("Output:", string) #printing string with "openstack" word replaced with "Azure"


inputString = input("Hello buddy, Enter your string: \n")
print("\nOption 1 is to 'Remove Unwated Text'\nOption 2 is to 'Remove numeric values'\nOption 3 is to 'Replace string with new string'\n")

Input = int(input("Enter option 1 or 2 or 3 as per your requirement: "))

p = StringFormatter(Input,inputString)