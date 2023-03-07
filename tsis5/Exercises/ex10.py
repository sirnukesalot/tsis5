#Write a Python program to convert a given camel case string to snake case.
import re
def tosnake(text):
    return re.sub('(?!^)([A-Z]+)', r'_\1',text).lower()
print(tosnake("IFeelAlive!"))