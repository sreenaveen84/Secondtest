"""from datetime import date
print(date.today().year)
#print(len((date.today().year)))"""

import re

string = "at what time?"
match = re.search('at',string)
print(match)
if (match):
    print("String found at: ",match.start())
else:
    print("String not found!")

