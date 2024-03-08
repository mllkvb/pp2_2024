#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
def test_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

specified_path = input("Input path: ")
test_path(specified_path)