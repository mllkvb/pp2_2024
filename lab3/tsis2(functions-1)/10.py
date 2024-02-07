def unilist(b):

    x = []
    for a in b:
       if a not in x:
           x.append(a) 
    return x

print(unilist([1,8,9,2,1,8,9,2])) 