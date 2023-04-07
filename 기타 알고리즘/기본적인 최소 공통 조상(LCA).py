import sys
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기
n = int(input())

# 트리에 대한 내용 입력
parent = [0] * (n + 1) # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부(True or False)
graph = [[] for _ in range(n + 1)] # 그래프(graph) 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].appen(b)
    graph[b].append(a)

# 루느 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth # 매번 노드에서 깊이 값을 기록
    # 이 노드와 인접한 다른 노드들을 하나씩 확인하면서
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        # 그렇지 않다면 인접한 노드에 대해서 현재까지 노드의 깊이에 +1하여 그 깊이로 대입
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이(depth)가 동일하도록
    while d[a] != d[b]:
        # 깊이가 큰 쪽을 부모쪽으로 이동하도록
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아질 때까지 부모 방향으로 동시에 이동하도록하여 최소 공통 조상을 찾기
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0) # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
