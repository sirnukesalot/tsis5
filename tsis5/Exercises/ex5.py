#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
def matches(text):
        pattern = 'a.*?b$'
        if re.search(pattern,  text):
                return 'Found!'
        else:
                return('Not found!')
print(matches("aaacccccb"))
print(matches("aaaccccd"))