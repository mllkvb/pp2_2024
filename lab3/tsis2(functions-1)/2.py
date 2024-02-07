def fahcel(Fah):
    c=(5 / 9) * (Fah - 32)
    return c
Fah=float(input())
cel=fahcel(Fah)
print(f"{Fah}degrees = {cel} degrees celcius")