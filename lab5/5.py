#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
a= open("row.txt","r",encoding ="UTF - 8 ")
s=a.read()
def str(txt):
    pattern = r"a.*b$"
    if re.search(pattern,txt):
        return "Yes, I Found"
    else:
        return "No, I couldn't find"
    
print(str(s))