# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드의 방문 정보를 표현(1차원 리스트)
visited = [False] * 9

def dfs(graph, v, visited):
    visited[v] = True # 방문한 노드 방문 처리
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)


dfs(graph, 1, visited) # 1은 최상단의 노드
