spy = 0
for x in range(0,len(numbers)-2):

    if numbers[x] == 0 and numbers[x+1] == 0 and numbers[x+2]==7:
        return True
return False