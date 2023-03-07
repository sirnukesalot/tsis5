#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
def matches(text):
        pattern = '^[A-Z]+[a-z]+$'
        if re.search(pattern,  text):
                return 'Found!'
        else:
                return('Not found!')
print(matches("Aa"))
print(matches("aaaaa"))
print(matches("aB"))