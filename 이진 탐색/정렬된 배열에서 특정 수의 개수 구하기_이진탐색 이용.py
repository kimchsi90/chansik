import sys
input = sys.stdin.readline

n, target = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search_left(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if target <= arr[mid]: # target 값을 찾았어도 더 작은 index를 가진 target 값을 찾기 위해(왼쪽 범위 탐색)
            end = mid - 1
            result = mid
        else:
            start = mid + 1
    return result

def binary_search_right(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= target: # target 값을 찾았어도 더 큰 index를 가진 target 값을 찾기 위해(오른쪽 범위 탐색)
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

print("right: ", binary_search_right(arr, target, 0, n)) # n의 가장 오른쪽 index 반환
print("left: ", binary_search_left(arr, target, 0, n)) # n의 가장 왼쪽 index 반환
print(binary_search_right(arr, target, 0, n) - binary_search_left(arr, target, 0, n) + 1)

result = binary_search_right(arr, target, 0, n) - binary_search_left(arr, target, 0, n)
if result == 0:
    print(-1)
else:
    print(result + 1) # n의 개수를 세는 것이므로 +1

'''
7 2
1 1 2 2 2 2 3

4
'''