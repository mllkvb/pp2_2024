#Write a Python program to drop microseconds from datetime.
import datetime
a=datetime.datetime.today().replace(microsecond=0)
print(a)