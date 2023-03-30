n = int(input())
data = list(input().split())

x, y = 0, 0
# R, L, D, U
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for vec in data:
    if vec == "R" and y < n:
        x += dx[0]
        y += dy[0]
    elif vec == "L" and y > 0:
        x += dx[1]
        y += dy[1]
    elif vec == "D" and x < n:
        x += dx[2]
        y += dy[2]
    elif vec == "U" and x > 0:
        x += dx[3]
        y += dy[3]

print(x + 1, y + 1)
