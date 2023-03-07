#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
def matches(text):
        pattern = 'ab{2,3}'
        if re.search(pattern,  text):
                return 'Found!'
        else:
                return('Not found!')
print(matches("abbbb"))
print(matches("abc"))