#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
s = input()
pattern = r"[ ,.]"

print(re.sub(pattern,":",s))