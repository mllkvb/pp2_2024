#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
s = input()
def ab(txt):
    pattern = r"ab{2,3}"
    if re.findall(pattern,txt):
        return "Yes, I Found"
    else:
        return "No, I couldn't find"

print(ab(s))