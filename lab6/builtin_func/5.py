def returning(tpl):
    return all(tpl)

string = input("Input: ")
tpl = tuple(map(lambda x: x == "True", string.split()))
print(f"Output: {returning(tpl)}")