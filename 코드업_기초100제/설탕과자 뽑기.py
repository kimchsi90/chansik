# https://codeup.kr/problem.php?id=6097

h, w = map(int, input().split())
n = int(input())

array = [[0] * w for _ in range(h)]

for _ in range(n):
    l, d, x, y = map(int, input().split())
    new_x, new_y = x - 1, y - 1
    for i in range(l):
        array[new_x][new_y] = 1
        if d == 0:
            new_y += 1
        else:
            new_x += 1

for i in range(h):
    for j in range(w):
        print(array[i][j], end=' ')
    print()
