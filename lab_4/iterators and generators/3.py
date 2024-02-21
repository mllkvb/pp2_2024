#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
n = int(input())
def generator(n):
    for i in range(0,n):
        if i %3 ==0 and i%4==0:
            yield i
        
for i in generator(n):
    print(i)


'''generator=(i for i in range(0,n) if i %3 ==0 and i%4==0)
for i in generator:
    print(i)'''