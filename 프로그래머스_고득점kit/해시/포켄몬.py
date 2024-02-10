from collections import Counter

def solution(nums):
    answer = 0
    
    # 가질 수 있는 포켄몬의 최대 종류 번호의 개수

    counter = Counter(nums)
    poke_dict = dict(counter)
    
    num_poke = len(nums)
    num_kinds = len(poke_dict)
    
    if num_poke >= num_kinds:
        return num_kinds
    else:
        return num_poke
    
    

print(solution([3, 1, 2, 3]))

# https://school.programmers.co.kr/learn/courses/30/lessons/1845