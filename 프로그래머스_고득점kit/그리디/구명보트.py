from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    dq = deque(people)
    
    while dq:
        if len(dq) == 1:
            dq.pop()
            answer += 1
        else:
            if dq[0] + dq[-1] > limit:
                dq.pop()
                answer += 1
            else:
                dq.popleft()
                dq.pop()
                answer += 1
        
    return answer

# 문제의 아이디어는 제일 가벼운 사람과 제일 무거운 사람의 합이 limit을 넘느냐 안 넘느냐를 가지고 결정해야 보트의 최솟값을 구할 수 있다는 점이다.
# https://school.programmers.co.kr/learn/courses/30/lessons/42885