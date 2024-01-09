n, target = map(int, input().split())

arr = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


result = binary_search(arr, target, 0, n - 1)

if result:
    print(result, '번째 위치에 존재합니다.')
else:
    print('원소가 존재하지 않습니다.')

'''
10 7
1 3 5 7 9 11 13 15 17 19

4

10 7
1 3 5 6 9 11 13 15 17 19
원소가 존재하지 않습니다.
'''