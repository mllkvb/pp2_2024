#Write a Python program to copy the contents of a file to another file
file1 = open('liverpool.txt', 'r')
file2 = open('liverpool_is_the_best_copy.txt', 'a')

for i in file1:
    file2.write(i)