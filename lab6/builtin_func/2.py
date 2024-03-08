def counting(string):
    up = 0
    low = 0
    
    for char in string:
        if char.isupper():
            up += 1
        elif char.islower():
            low += 1
    
    return up, low
    
string = input("Input: ")
up_count, low_count = counting(string)
print(f"Number of upper chars: {up_count}")
print(f"Number of lower chars: {low_count}")
