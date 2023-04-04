# 특정 원소가 속한 집합을 찾기
# 특정 원소가 속한 루트 번호를 반환하는 함수
def find_parent(parent, x): # parent: 부모 테이블, x: 노드 번호
    # 루트 노드를 찾을 때까지 재귀 호출
    # 현재 부모가 자기 자신이 아니라면 루트 노드가 아니라는 의미기 때문에 부모에 대한 노드 번호를 넣어서 다시 find_parent 함수 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 경로 압축(Path Compression) 적용
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    # 부모 테이블에 적혀있는 부모의 값이 자신의 루트가 될 수 있도록 설정하는 것
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a) # a의 루트 노드
    b = find_parent(parent, b) # b의 루트 노드
    # 번호가 큰 쪽이 작은 쪽을 부모로 선택
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수를 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 간선의 개수에 따라. 즉, 두 원소를 연결하고 있는 각각의 연결 여부를 확인하면서 Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b) # 원소 a, b가 서로 연결되어 있다는 의미로 union_parent 함수 호출

# 각 원소가 속한 집합 출력하기
# 각 노드에 대한 루트 노드가 출력 됨(find_parent)
# 루트 노드가 같은 원소 끼리는 같은 집합임
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
# 자신의 부모에 대한 내용으로 이 값이 자신의 루트 즉, 집합에 대한 정보가 아닐 수 있다는 점 참고해야 함
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
