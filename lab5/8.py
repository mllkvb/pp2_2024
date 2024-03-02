#Write a Python program to split a string at uppercase letters.
import re
a= open("row.txt","r",encoding ="UTF - 8 ")
s=a.read()

def split(str):
    split=re.findall(r"[A-Z][^A-Z]*",str)
    return split

print(split(s))