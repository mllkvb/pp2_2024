#Write a Python program to calculate two date difference in seconds.
from datetime import datetime
def dd(d1,d2):
    difference=d1-d2
    return difference.total_seconds()

d1=datetime(2024,2,18,12,0,0)
d2=datetime(2024,2,17,12,0,0)
dds =dd(d1,d2)
print(dds)