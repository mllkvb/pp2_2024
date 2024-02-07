def recipe(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = 1892
ounces = recipe(grams)
print(f"{grams} grams = {ounces} ounces")