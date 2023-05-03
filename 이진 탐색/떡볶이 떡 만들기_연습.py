import sys
input = sys.stdin.readline

n, target = map(int, input().split())
arr = list(map(int, input().split()))

def cut_ricecake(arr, height):
    result = 0
    for ricecake in arr:
        if ricecake - height > 0:
            result += ricecake - height
    return result

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = cut_ricecake(arr, mid)
        if  total >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

print(binary_search(arr, target, 0, max(arr)))

'''
4 6
19 15 10 17
'''