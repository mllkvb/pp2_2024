#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re 
a = open("row.txt", "r" , encoding = "UTF - 8")
s = a.read()

def find(txt):
    pattern = r"[A-Z][a-z]+"
    match = re.findall(pattern, txt)
    return match

print(find(s))