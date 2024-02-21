#Create a generator that generates the squares of numbers up to some number N.
n = int(input())
def generator(n):
    for  i in range(n):
        yield i*i

for i in generator(n):
    print(i)