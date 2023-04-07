import sys

input = sys.stdin.readline # 시간 초과를 피하기 위한 빠른 입력 함수
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정
LOG = 21 # 2^20 = 1,000,000

# 트리에 대한 정보 받기
n = int(input())
parent = [[0] * LOG for _ in range(n + 1)] # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부(True or False)
graph = [[] for _ in range(n + 1)] # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        # 2^0 즉, 한 칸 위의 부모만 먼저 구해서 넣기
        parent[y][0] = x
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하는 함수
# DP를 이용해 2의 제곱 꼴로 건너 뛰었을 때 부모를 기록
def set_parent():
    dfs(1, 0) # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# A와 B의 최소 공통 조상을 찾는 함수
# lca 함수는 O(logN)의 시간 복잡도를 가지게 됨(2의 제곱 꼴로 줄어들도록하기 때문)
def lca(a, b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    # 큰 값부터 작은 값까지 줄이면서 확인
    for i in range(LOG - 1, -1, -1):
        # 깊이를 구하고 그 차이가 충분히 크다면 2의 제곱 꼴만큼 감소하도록 만들어서 더 깊은 쪽이 깊이가 줄어들 수 있도록 한다. ex) 깊이가 15라면 8 -> 4 -> 2 -> 1 이렇게 줄어들게 하여 4번 만에 15만큼 줄이도록
        if d[b] - d[a] > (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    # 부모가 같다면 리턴
    if a == b:
        return a
    # 부모가 같지 않다면
    # 2의 제곱 형태에서 큰 값부터 차례대로 작은 값을 확인해서 거슬러 올라가도록
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
