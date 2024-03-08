#Write a Python program to count the number of lines in a text file.
import os

f = open(r" /Users/milekbaibolat/kbtu/pp2 /lab6/dir_and_files/3.py", "r")
counter = 0
for x in f:
    counter += 1

print(counter)