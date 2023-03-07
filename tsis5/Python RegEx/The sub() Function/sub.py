#The sub() function replaces the matches with the text of your choice:

#Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#You can control the number of replacements by specifying the count parameter:

#Replace the first 2 occurrences:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)