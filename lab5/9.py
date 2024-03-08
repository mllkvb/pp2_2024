#Write a Python program to insert spaces between words starting with capital letters.
import re
s=input()
def insert(str):
    caplet=re.sub(r"(\w)([A-Z])",r"\1 \2",str)
    return caplet

print(insert(s))