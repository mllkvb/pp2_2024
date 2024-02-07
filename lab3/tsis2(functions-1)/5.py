def permutations(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            permutations(s[:i] + s[i+1:], prefix + s[i])


inputs = input()
print()
permutations(inputs)
