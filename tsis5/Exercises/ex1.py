#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
def matches(text):
        pattern = '^a(b*)$'
        if re.search(pattern,  text):
                return 'Found!'
        else:
                return('Not found!')
print(matches("abc"))
print(matches("abbbb"))