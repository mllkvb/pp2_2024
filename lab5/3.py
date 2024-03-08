#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re 
s = input()
def lowercase(txt):
    return re.findall(r"[a-z]+_+[a-z]+",txt)

print(lowercase(s))