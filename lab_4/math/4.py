#Write a Python program to calculate the area of a parallelogram
import math
def area_parallelogram(b,h):
    return b*h
b=int(input("length:"))
h=int(input("heigth:"))
area= area_parallelogram(b,h)
print(float(area))