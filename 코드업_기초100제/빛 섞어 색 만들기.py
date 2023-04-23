# https://codeup.kr/problem.php?id=6083

red, green, blue = map(int, input().split())

r_arr = [i for i in range(red)]
g_arr = [i for i in range(green)]
b_arr = [i for i in range(blue)]

for r in r_arr:
    for g in g_arr:
        for b in b_arr:
            print(f"{r} {g} {b}")
print(len(r_arr) * len(g_arr) * len(b_arr))
