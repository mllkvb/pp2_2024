#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
s = input()
pattern = r"a.*b$"

print(re.findall(pattern,s))