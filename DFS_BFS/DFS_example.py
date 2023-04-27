# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [], # 그래프의 번호가 1번부터 시작하는 경우가 많기 때문에 0번 인덱스는 비워둔다
    [2, 3, 8],  # 1번 인덱스인 1번 노드의 인접한 노드를 리스트 형태로 담아줌
    [1, 7], 
    [1, 4, 5], 
    [3, 5], 
    [3, 4], 
    [7], 
    [2, 6, 8], 
    [1, 7]
    ]

# 각 노드의 방문 정보를 표현(1차원 리스트)
visited = [False] * 9

def dfs(graph, v, visited):
    visited[v] = True # 방문한 노드 방문 처리
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited) # 1은 최상단의 노드
