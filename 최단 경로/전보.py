import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단거리는 0으로 설정하여 우선순위 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면 계속 반복
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 처리된 적이 있는 노드라면 무시
        if distance[now] > dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        # i는 now에서 (인접한 노드, 거리)
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 최단 거리 테이블 갱신 및 우선 순위 큐에 추가
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m, start = map(int, input().split())
# 각 노드에 연결 돼있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c라는 의미
    # tuple로 입력할 경우 0번째 인덱스인 b를 이용하여 우선 순위를 정할 수 있음
    graph[a].append((b, c))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)
