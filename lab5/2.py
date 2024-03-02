#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
a = open("row.txt", "r", encoding="UTF-8")
s = a.read()
def ab(txt):
    pattern = "ab{2,3}"
    if re.fullmatch(pattern,txt):
        return "Yes, I Found"
    else:
        return "No, I couldn't find"

print(ab(s))