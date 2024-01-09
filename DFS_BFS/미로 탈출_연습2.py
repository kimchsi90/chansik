# 괴물이 있는 부분은 0, 없는 부분은 1
# 1, 1에서 시작
# 미로의 출구는 n, m
# 한 번에 한 칸씩 이동
# 최소 칸의 개수는?, 시작 칸과 마지막 칸을 모두 계산

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
result = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    arr[x][y] = 1

    while queue:
        vx, vy = queue.popleft()

        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = arr[vx][vy] + 1
                queue.append((nx, ny))

    return arr[n - 1][m - 1]

print(arr)   
print(bfs(0, 0))


'''
5 6
101010
111111
000001
111111
111111

10
'''