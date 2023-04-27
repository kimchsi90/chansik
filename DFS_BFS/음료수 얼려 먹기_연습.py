
n, m = map(int, input().split()) # 1<=N,M<=1,000이므로 전체 얼음틀의 공간은 100만개가 됨
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False
    
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)

'''
4 5
00110
00011
11111
00000
'''