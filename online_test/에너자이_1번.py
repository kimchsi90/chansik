def solution(n,m):
    answer = 0
    
    for num in range(n, m + 1):
        if num <= 9:
            answer += 1
            continue

        str_n = str(num)
        is_palindome = False

        for i in range(len(str_n) // 2):
            if str_n[i] == str_n[-1 - i]:
                is_palindome = True
            else:
                is_palindome = False
                break

        if is_palindome:
            answer += 1
                   
    return answer
