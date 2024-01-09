n = int(input())
arr = list(input().split())

x, y = 1, 1

# 방향벡터 RLDU순
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for dir in arr:
    if dir == 'R':
        new_x, new_y = x + dx[0], y + dy[0]
    elif dir == 'L':
        new_x, new_y = x + dx[1], y + dy[1]
    elif dir == 'D':
        new_x, new_y = x + dx[2], y + dy[2]
    elif dir == 'U':
        new_x, new_y = x + dx[3], y + dy[3]
    if 0 < new_x <= n and 0 < new_y <= n:
        x, y = new_x, new_y

print(x, y)


# move types list 추가한 경우 구현

dx = [0, 0, 1, -1] # 열
dy = [1, -1, 0, 0] # 행
move_types = ['R', 'L', 'D', 'U']

for i in arr:
    for j in range(len(move_types)):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    
    if 0 < nx <= n and 0 < ny <= n:
        x, y = nx, ny

print(x, y)