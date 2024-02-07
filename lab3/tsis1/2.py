class Shape:
    def area(self):
        return 0
class Square:
    def __init__(self,lenght):
        self.lenght=lenght
    def area(self):
        return self.lenght ** 2

a=Shape()
print(a.area())
b=Square(8)
print(b.area())