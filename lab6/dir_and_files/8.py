#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

path = input()

if os.path.exists(path):
    os.remove(path)
else:
    print("No such file was found!") 