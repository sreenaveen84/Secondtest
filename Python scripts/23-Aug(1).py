import re
class StringFormatter:
    def remove_unwanted_text():
        #original string with unwanted chars
        originalString = "m$%y &nam12e is A^le%x"

        # printing original string
        print ("Original String : ", originalString)

        required_string = re.sub(r"[^a-zA-Z.\s]",'',originalString)

        print ("Required string is : ", str(required_string))
    def remove_numeric_values():
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
    def replace_string_with_required_string():
        string = "Altiostar vcu and vdu deployment on openstack"

        print("Input:", string) #printing original string

        string = string.replace('openstack', 'Azure')

        print("Output:", string) #printing string with "openstack" word replaced with "Azure"



StringFormatter.remove_unwanted_text();
StringFormatter.remove_numeric_values();
StringFormatter.replace_string_with_required_string();