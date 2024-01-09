# 우선순위 큐를 이용

from heapq import *

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n

    h = []

    for i in range(n): # 시간복잡도 N
        value = numbers[i]

        while h and h[0][0] < value:
            _, idx = heappop(h)
            answer[idx] = value

        heappush(h, [value, i])

    return answer

print(solution([2, 4, 2, 5]))