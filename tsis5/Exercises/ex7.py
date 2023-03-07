#Write a python program to convert snake case string to camel case string.
import re
def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:]) 
print(to_camel_case("good_idea_everyone"))