def solution(price):
    answer = [-1] * len(price)
    stack = []

    for i in range(len(price)):
        while stack:
            j = stack[-1]
            if price[j] < price[i]:
                answer[j] = i - j
                stack.pop()
            else:
                break
        stack.append(i)

    return answer


print(solution([13, 7, 3, 7, 5, 16, 12]))

# stack에 쌓이는 원소들은 다음 인덱스의 값보다 작은 것들만 들어감
# stack의 -1 인덱스만 확인해도 되는 이유는 -1 인덱스 값이 항상 가장 작기 때문에
# 시간 복잡도: O(N)
# price의 길이 N만큼 반복문 수행하고 for문 내부의 것들은 상수기 때문에
# 공간 복잡도: O(1)
# answer, stack, i, j 등의 변수에 값이 저장되므로

'''
[4, 1, 4, 7, 6]
[3, 1, 1, -1, -1]

[13, 7, 3, 7, 5, 16, 12]
[5, 4, 1, 2, 1, -1, -1]
'''