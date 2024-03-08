#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

path = input()

with os.scandir(path) as it:
    for x in it:
        if(x.is_dir()):
            print(x.name)
print(" ")
with os.scandir(path) as it:
    for x in it:
        if(not x.is_dir()):
            print(x.name)
print(" ")
with os.scandir(path) as it:
    for x in it:
        print(x.name)