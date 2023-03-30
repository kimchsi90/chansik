from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(
        list(map(int, input()))
    )  # 한 개 row에 0과 1로 이루어진 문자열이 들어오므로 문자열의 각 원소에 int를 적용하여 list로 만드는 과정

# 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    # 좌표이므로 튜플로 넣어주기
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드 하나를 꺼내 그 노드를 기준으로 4가지 방향에 대하여 방문한 적이 없고 이동할 수 있는 노드에 대해 시작점으로부터의 거리 값을 넣어주고 그 좌표를 큐에 넣어줌
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 밖으로 이동할 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))  # 좌표 튜플
    return graph[n - 1][m - 1]


print(bfs(0, 0))
