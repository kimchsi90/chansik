# 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제

import sys
import heapq
input = sys.stdin.readline

# python의 heap 자료구조는 min heap이기 때문에 오름차순 정렬됨
# python에서 내림차순 정렬을 하려면 heap에 넣고 빼는 원소에 -부호를 붙이면 됨(max heap으로 동작)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])
