#Write a Python program to insert spaces between words starting with capital letters.
import re
a= open("row.txt","r",encoding ="UTF - 8 ")
s=a.read()

def insert(str):
    caplet=re.sub(r"([A-Z][a-z]+)",r"\1",str)
    return caplet

print(insert(s))