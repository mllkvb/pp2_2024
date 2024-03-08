#Write a Python program to split a string at uppercase letters.
import re

s = input()
pattern = r"[A-Z]{1}[a-z]*"
split=re.findall(pattern,s)

print(split)