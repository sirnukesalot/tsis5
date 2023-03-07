#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
def matches(text):
        pattern = '^[a-z]+_[a-z]+$'
        if re.search(pattern,  text):
                return 'Found!'
        else:
                return('Not found!')
print(matches("abb_ccc"))
print(matches("a_Abbc"))
print(matches("Aaaa_aaa"))