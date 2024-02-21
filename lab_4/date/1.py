#Write a Python program to subtract five days from current date.
from datetime import date , timedelta
dt=date.today()-timedelta(5)
print(date.today())
print(dt)