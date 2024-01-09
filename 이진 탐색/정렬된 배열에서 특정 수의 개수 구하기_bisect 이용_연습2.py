from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

# 입력 조건: 수열은 오름차순 정렬된 상태로 입력이 된다.
# 출력 조건: 수열의 원소 중에서 값이 x인 원소의 개수를 출력. 단, 값이 x인 원소가 하나도 없을 경우 -1을 출력

# n의 개수가 최대 1,000,000이므로 O(logN)으로 동작하는 탐색 알고리즘을 사용하지 않으면 시간 초과 발생
# 일반적인 선형 탐색 알고리즘을 사용하면 시간 초과 발생

def search(target):
    result = bisect_right(arr, target) - bisect_left(arr, target)

    if result == 0:
        return -1
    else:
        return result

print(search(x))



'''
7 2
1 1 2 2 2 2 3

4
'''