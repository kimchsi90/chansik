# 데이터 업데이트가 가능한 상황에서의 구간 합(Interval Sum)을 바이너리 인덱스 트리(Binary Indexed Tree)를 이용하여 구하기

# https://www.acmicpc.net/problem/2042

import sys
input = sys.stdin.readline

# 데이터의 개수(n), 변경 횟수(m), 구간 합 계산 횟수(k)
# 5, 2, 2
n, m, k = map(int, input().split())

# 전체 데이터의 개수는 최대 1,000,000개
arr = [0] * (n + 1) # 각각의 데이터에 대한 값을 담는 배열
tree = [0] * (n + 1) # BIT에 대한 정보를 담는 배열

# i번째 수까지의 누적 합을 계산하는 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 왼쪽으로 이동
        i -= (i & -i)
    return result

# i번째 수를 특정 값(dif)만큼 더하는 함수
def update(i, dif):
    while i <= n:
        # 트리에서 0이 아닌 마지막 비트만큼 더해가면서 오른쪽으로 이동하며 각각의 인덱스에 대해서 얼만큼의 값을 더해줄 지 적용하는 것
        tree[i] += dif
        i += (i & -i)

# start부터 end까지의 구간 합을 계산하는 함수
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1, n + 1):
    x = int(input()) # 1, 2, 3, 4, 5
    arr[i] = x
    update(i, x)

for i in range(m + k):
    # 1 3 6
    # 2 2 5
    # 1 5 2
    # 2 3 5
    a, b, c = map(int, input().split())
    # 업데이트(update) 연산인 경우
    if a == 1:
        update(b, c - arr[b]) # 바뀐 크기(dif) 만큼 적용
        arr[b] = c
    # 구간 합(interval sum) 연산인 경우
    else:
        print(interval_sum(b, c))
