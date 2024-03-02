#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
a= open("row.txt","r",encoding ="UTF - 8 ")
s=a.read()

def replace(txt):
    pattern = r"[ ,.]"
    replace = re.sub(pattern, ":" ,txt)
    return replace

print(replace(s))