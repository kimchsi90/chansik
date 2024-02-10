from collections import defaultdict

def solution(clothes):
    answer = 1
    # 하루에 최소 한 개의 의상을 입음
    # 하나라도 다르면 다른 옷을 착용한 것
    # 종류별 최대 1가지만 착용 가능
    dict_cloth = defaultdict(list)

    for c in clothes:
        dict_cloth[c[1]].append(c[0])
    
    for key in dict_cloth.keys():
        answer *= len(dict_cloth[key]) + 1

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 모든 key 값들에 대한 개수 + 1(안 입는 경우) 값을 모두 곱하고
# 아무것도 안 입는 경우인 1을 빼면 된다.