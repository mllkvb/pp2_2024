#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
n =int(input())
def my_generator(n):

    value = 0
    while value < n:
         yield value
         value += 2

for value in my_generator(n):
    print(value)