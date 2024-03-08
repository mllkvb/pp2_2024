#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
def check_path_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    
    print(f"Path '{path}' exists.")

    if os.access(path, os.R_OK):
        print("Readable: Yes")
    else:
        print("Readable: No")

    if os.access(path, os.W_OK):
        print("Writable: Yes")
    else:
        print("Writable: No")

    if os.access(path, os.X_OK):
        print("Executable: Yes")
    else:
        print("Executable: No")

specified_path = input("Input path: ")
check_path_access(specified_path)