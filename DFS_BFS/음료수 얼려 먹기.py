n, m = map(int, input().split()) # 1<=N,M<=1,000이므로 전체 얼음틀의 공간은 100만개가 됨

graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if not (0 <= x < n and 0 <= y < m):
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
        # 현재 위치를 방문하지 않았다면 True를 반환하고 현재 위치와 인접한 모든 노드를 방문 처리
        if dfs(i, j) == True:
            result += 1

print(result)

'''
4 5
00110
00011
11111
00000

정답: 3
'''