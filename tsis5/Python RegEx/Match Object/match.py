#A Match Object is an object containing information about the search and the result.

#Note: If there is no match, the value None will be returned, instead of the Match Object.

#Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

#The Match object has properties and methods used to retrieve information about the search, and the result:

#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

#Print the position (start- and end-position) of the first match occurrence.
#The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#Print the string passed into the function:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#Print the part of the string where there was a match.
#The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

#Note: If there is no match, the value None will be returned, instead of the Match Object.