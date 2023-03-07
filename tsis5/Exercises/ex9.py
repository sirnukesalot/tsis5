#Write a Python program to insert spaces between words starting with capital letters.
import re
def capitals(text):
   return re.sub(r"\B([A-Z])", r" \1",text)
print(capitals("PushThatCart"))