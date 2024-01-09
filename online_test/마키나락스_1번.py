def solution(s):
    answer = 0
    for i in range(len(s) - 1):
        if (i + answer) % 2 == 0:
            if s[i] >= s[i+1]:
                answer += 1
        else:
            if s[i] <= s[i+1]:
                answer += 1

    return answer

print(solution([1, 2, 3]))

# 시간 복잡도: O(s)
# list s의 길이만큼 for문이 반복되고 for문의 내부는 조건문과 비교 연산, 변수에 1을 더하는 부분이므로 상수

# 공간 복잡도: O(1)
# 알고리즘과 유관한 가변 공간은 없고, 알고리즘과 무관한 고정 공간은 변수밖에 없으므로

'''
[1, 2, 3]
1

[3, -1, 0, 4]
2
'''