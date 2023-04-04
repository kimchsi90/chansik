import sys
input = sys.stdin.readline
INF = int(1e9)
# 노드의 개수와 간선의 개수 입력
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)을 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for i in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    # a에서 b로 가는 시간은 1이라는 의미
    graph[a][b] = 1
    graph[b][a] = 1 # 양방향 이동이 가능하기 때문에 이 부분 추가

# X와 K 입력
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1): # k: 거쳐가는 노드
    for a in range(1, n + 1): # a: 출발 노드
        for b in range(1, n + 1): # b: 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간 출력(만약 도달할 수 없다면 -1을 출력)
distance = graph[1][k] + graph[k][x] 
if distance >= INF:
    print("-1")
else:
    print(distance)
