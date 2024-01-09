arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0] # list slice
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot] # list comprehension
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))
