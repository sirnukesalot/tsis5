#The findall() function returns a list containing all matches.

#Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#The list contains the matches in the order they are found.

#If no matches are found, an empty list is returned:

#Return an empty list if no match was found:

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)