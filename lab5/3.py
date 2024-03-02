#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re 
a = open("row.txt", "r" , encoding = "UTF - 8")
s = a.read()

def lowercase(txt):
    return re.findall(r"\b[a-z]+_[a-z]+\b",txt)

print(lowercase(s))