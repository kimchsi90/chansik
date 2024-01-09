def solution(clothes):
    answer = 1
    dict_clo = {}
    
    for cloth in clothes:
        if cloth[-1] in dict_clo:
            dict_clo[cloth[-1]] += (len(cloth) - 1)
        else:
            dict_clo[cloth[-1]] = len(cloth) - 1
    
    for n in dict_clo.values():
        answer *= (n + 1) # 각 종류의 수에 아무것도 착용하지 않는 경우의 수 1을 더한 값을 곱하여 모든 경우의 수를 구한다

    return answer - 1 # 하나도 입지 않은 경우 1을 뺀다


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))


'''
https://school.programmers.co.kr/learn/courses/30/lessons/42578

[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
5

[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
3

의상의 종류 별로 하나도 안 입은 경우까지 1더하여 모든 의상 종류에 대한 모든 경우의 수를 구하고
아무것도 착용하지 않은 경우의 수 1을 빼서 정답을 구함
'''