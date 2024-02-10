def solution(n, lost, reserve):
    # 학생들 번호 체격순, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 빌려줄 수 있음
    # 4번이 3이나 5한테만
    # 최대한 많은 학생이 빌려야함
    # 체육수업을 들을 수 있는 학생의 최댓값을 return
    # 잃어버린 학생 수 빼기
    
    common_elements = set(lost) & set(reserve)
    
    lost = [item for item in lost if item not in common_elements]
    reserve = [item for item in reserve if item not in common_elements]
    
    lost.sort()
    reserve.sort()
    
    for i in reserve.copy():
        for j in lost.copy():
            if (i - 1 == j) or (i + 1 == j):
                reserve.remove(i)
                lost.remove(j)
                break
    
    return n - len(lost)