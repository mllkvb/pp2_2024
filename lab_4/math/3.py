#Write a Python program to calculate the area of regular polygon.\
import math
def area_of_rpolygon(n,l):
    return n * (l**2)/4 * math.tan(math.pi / n)
n=int(input("Number of sides:"))
l=int(input("Length of a side:"))
area=area_of_rpolygon(n,l)
print(math.ceil(area))