def solution(n, lost, reserve):
    answer = n - len(lost) # 전체 학생 중 체육복 없는 애들 빼기
    lost.sort()
    reserve.sort()
    
    for lp in lost.copy():
        if lp in reserve: # 여유분있는 동시에 잃어버린 사람 먼저 lost, reserve에서 제거
            reserve.remove(lp)
            lost.remove(lp)
            answer += 1
            
    for lp in lost:
        if (lp - 1) in reserve:
            reserve.remove(lp - 1)
            answer += 1
        elif (lp + 1) in reserve:
            reserve.remove(lp + 1)
            answer += 1
            
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42862