#Write a Python program to print yesterday, today, tomorrow.
from datetime import date,timedelta
today = date.today()
yesterday=date.today()-timedelta(1)
tomorrow=date.today()+timedelta(1)
print(today)
print(yesterday)
print(tomorrow)