#Write a Python program to drop microseconds from datetime.
from datetime import datetime
a=datetime.now().replace(microsecond=0)
print(a)