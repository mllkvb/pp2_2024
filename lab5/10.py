#Write a Python program to convert a given camel case string to snake case.
import re
a= open("row.txt","r",encoding ="UTF - 8 ")
s=a.read()

def camel_to_snake(txt):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake(s))