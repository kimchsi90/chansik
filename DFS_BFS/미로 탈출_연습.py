from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
# 괴물 있:0, 없:1

# 탈출 위해 움직여야 하는 최소 칸의 개수(시작, 마지막 포함)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    dq = deque([(x, y)])
    while dq:
        a, b = dq.popleft()
        for dir in dirs:
            nx = a + dir[0]
            ny = b + dir[1]
            if not (0 <= nx <= (n - 1) and 0 <= ny <= (m - 1)):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                dq.append((nx, ny))
    return graph[n - 1][m - 1]
                

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