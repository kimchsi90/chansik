
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print(selection_sort(arr))

'''
시간 복잡도
N + (N - 1) + ... + 2 = N(N + 1)/2 - 1 = (N**2 + N - 2)/2 -> BigO notation에 따라 O(N**2)라고 작성

'''