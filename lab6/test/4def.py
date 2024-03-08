n = int(input())
def generator(n):
    for  i in range(0,n):
        if i % 10 == 4:
            yield i

for i in generator(n):
    print(i)