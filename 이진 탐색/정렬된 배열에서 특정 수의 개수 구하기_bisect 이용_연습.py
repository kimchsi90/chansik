from bisect import bisect_left, bisect_right

def count_by_range(arr, left_value, right_value):
    return bisect_right(arr, right_value) - bisect_left(arr, left_value)


arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(arr, 4, 4))

print(count_by_range(arr, -1, 3)) # -1 임에 주의
