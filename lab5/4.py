#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re 
s = input()
pattern=r"[A-Z][a-z]+"

print(re.findall(pattern,s))