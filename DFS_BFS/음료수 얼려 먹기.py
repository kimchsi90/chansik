n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y <= n:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        # 인접한 모든 노드의 방문 처리를 수행
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치를 방문하지 않았다면 True 반환하 현재 위치와 인접한 모든 노드를 방문 처리
        if dfs(i, j) == True:
            result += 1

print(result)
