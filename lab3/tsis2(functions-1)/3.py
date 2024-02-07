def solve(numheads, numlegs):
    
    chickens = 0
    rabbits = numheads
    
    while rabbits >= 0:
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
        chickens += 1
        rabbits -= 1
    
    return "No "


numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print() #chickens
print() #rabbits
