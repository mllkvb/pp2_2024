#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
a = open("row.txt", "r", encoding="UTF-8")
s = a.read()

reg =r"/w*ab*/w*"
print(re.findall(reg, s))