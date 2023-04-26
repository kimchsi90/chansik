# 2차원 방향 벡터를 이용하여 움직임 조절

n = int(input())
data = list(input().split())
arr = [[] * (n + 1) for _ in range(n + 1)]

# R L D U
dx = [0, 0, 1, -1] # 열
dy = [1, -1, 0, 0] # 행
move_types = ["R", "L", "D", "U"]

x, y = 1, 1

for dir in data:
    for i in range(len(move_types)):
        if dir == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if n >= nx >= 1 and n >= ny >= 1:
        x, y = nx, ny

print(x, y)
