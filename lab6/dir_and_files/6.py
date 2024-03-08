#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os

for i in range(65, 91):
    f = open(chr(i) + ".txt", "x")