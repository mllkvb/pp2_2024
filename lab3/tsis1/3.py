class Shape:
    def area(self):
        return 0
class Rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width 
    def area(self):
        return self.lenght *self.width
s=Shape()
print(s.area())
r=Rectangle(5,6)
print(r.area())