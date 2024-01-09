n, x = map(int, input().split())
arr = list(map(int, input().split()))

# 입력 조건: 수열은 오름차순 정렬된 상태로 입력이 된다.
# 출력 조건: 수열의 원소 중에서 값이 x인 원소의 개수를 출력. 단, 값이 x인 원소가 하나도 없을 경우 -1을 출력

# n의 개수가 최대 1,000,000이므로 O(logN)으로 동작하는 탐색 알고리즘을 사용하지 않으면 시간 초과 발생
# 일반적인 선형 탐색 알고리즘을 사용하면 시간 초과 발생

''' 이진탐색 반복문 구현'''
# def right_bin_search(target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
        
#         if arr[mid] <= target:
#             start = mid + 1
#             right_idx = mid
#         else:
#             end = mid - 1

#     if arr[right_idx] == target:
#         return right_idx
#     else:
#         return None


# def left_bin_search(target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
        
#         if arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#             left_idx = mid

#     if arr[left_idx] == target:
#         return left_idx
#     else:
#         return None

left_idx, right_idx = 0, 0

'''이진탐색 재귀적 구현'''
def right_bin_search(target, start, end):
    global right_idx
    if start > end: # 재귀함수를 사용할 땐 시작 부분에 종료 조건을 반드시 넣어줘야 함
        if target == arr[right_idx]:
            return right_idx
        return 0
    
    mid = (start + end) // 2

    if arr[mid] <= target:
        right_idx = mid
        return right_bin_search(target, mid + 1, end)
    else:
        return right_bin_search(target, start, mid - 1)


def left_bin_search(target, start, end):
    global left_idx
    if start > end:
        if target == arr[left_idx]:
            return left_idx
        else:
            return 0
    
    mid = (start + end) // 2

    if target <= arr[mid]:
        left_idx = mid
        return left_bin_search(target, start, mid - 1)
    else:
        return left_bin_search(target, mid + 1, end)


def search(target, start, end):
    right_idx = right_bin_search(target, start, end)
    left_idx = left_bin_search(target, start, end)

    if right_idx == 0 or left_idx == 0:
        return -1
    else:
        return right_idx - left_idx + 1

print(search(x, 0, len(arr) - 1))


'''
7 2
1 1 2 2 2 2 3

4
'''