from collections import Counter

def solution(participant, completion):

    # 완주하지 못한 선수의 이름 return
    # 동명이인 있음

    p_counter = Counter(participant)
    c_counter = Counter(completion)

    diff = p_counter - c_counter
    
    return list(diff)[0]


print(solution(["mislav", "stanko", "mislav", "ana"], ["mislav", "stanko", "ana"]))

# https://school.programmers.co.kr/learn/courses/30/lessons/42576