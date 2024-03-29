#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s
import re
s = input()
reg =r"ab*"

print(re.findall(reg, s))
