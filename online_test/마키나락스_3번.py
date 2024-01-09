from collections import deque
import time
from random import randint, seed
seed(42)

# p = [randint(1, 1_000_000) for _ in range(100_000)]
p = [103,101,103,103,101,102,100,100,101,104]


def solution(p):
    answer = 0
    p.sort()
    dq = deque(p)

    while dq: # O(n)
        curr = dq.popleft() # O(1)
        for item in dq.copy(): # O(n)
            if curr < item: # O(1)
                dq.remove(item) # O(n)
                curr = item # O(1)
                answer += 1 # O(1)
    return answer

start_time = time.time()
print(solution(p))
# print(f"{time.time() - start_time}")

# 문제 해결 아이디어
# 정렬하여 작은 값부터 뒤의 모든 원소들을 확인하여 자기보다 큰 값이 있으면 값을 소거하면서 answer += 1
# list의 pop(0)은 모든 뒤의 원소들을 앞으로 당겨야하기 때문에 O(n)의 시간 복잡도가 소요
# deque의 popleft()는 O(1)의 상수

# 시간복잡도: O(n**3)
# while문이 n번 돌고, for문이 n-1번 돌다가 조건이 맞으면 dq.remove()하므로 최악의 경우 O(n**3)이 될 수 있음
# 공간복잡도: O(1)
# p, answer, dq, curr, item이 모두 변수이므로


'''
[3,2,1,4.5]
4

[20,10,10,20]
2

[103,101,103,103,101,102,100,100,101,104]
7
'''