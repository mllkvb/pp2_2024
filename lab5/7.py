#Write a python program to convert snake case string to camel case string.
import re
a= open("row.txt","r",encoding ="UTF - 8 ")
s=a.read()
def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel(s))