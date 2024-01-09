from collections import deque

# n: 행, m: 열
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
result = 0

# 구멍이 뚫린 부분이 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, graph):
    queue = deque([(x, y)])
    graph[x][y] = 1

    while queue:
        vx, vy = queue.popleft()

        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[vx][vy] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if not arr[i][j]: # 구멍이 뚫린 부분이라면
            bfs(i, j, arr)
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

# def dfs(x, y):
#     if (0 <= x < n) and (0 <= y < m) and not arr[x][y]:
#         arr[x][y] = 1 # 방문 처리
#         print(f'{x}, {y}')
        
#         dfs(x, y + 1)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x - 1, y)

# for i in range(n):
#     for j in range(m):
#         if not arr[i][j]: # 방문한 곳이 0이면(뚫린 곳이라면)
#             dfs(i, j)
#             result += 1
#             print()

# print(result)



# dfs, bfs 기본 연습

# def dfs(graph, start, visited):
#     visited[start] = True
#     print(start, end = ' ')

#     for i in graph[start]:
#         if not visited[i]:
#             visited[i] = True
#             print(i, end = ' ')
#             dfs(graph, i, visited)


# def bfs(graph, start, visited):
#     queue = deque([start]) # Step1. 큐에 원소를 삽입하고 
#     visited[v] = True # 방문처리합니다.
    
#     while queue: # 더 이상 Step2 과정을 수행할 수 없을 때까지 반복합니다.
#         v = queue.popleft() # Step2. 큐에 들어있는 원소를 꺼내고

#         for i in graph[i]: # 인접 노드 중에서
#             if not visited[i]: # 방문하지 않은 노드를
#                 queue.append(i) # 모두 큐에 넣고
#                 visited[i] = True # 방문처리 합니다.
