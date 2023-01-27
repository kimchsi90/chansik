n = int(input())
coin_types = [500, 100, 50, 10]

count = 0

for coin in coin_types:
    div, mod = divmod(n, coin)
    count += div
    n = mod
    print(f"{coin}: {div}")

print(f"\ncount: {count}")
