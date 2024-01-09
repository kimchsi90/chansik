arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def insertion_sort(arr):
    for i in range(1, len(arr)): # 1 ~ 9
        for j in range(i, 0, -1): # i ~ 1
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break

    return arr

print(insertion_sort(arr))

'''
시간 복잡도
직관적으로 안쪽 for문을 보면 비교 연산자와 swap 연산밖에 없기 때문에 O(N**2)라고 할 수 있다.

삽입정렬은 최선의 경우 O(N)의 시간 복잡도를 가지는데
정렬할 리스트가 이미 정렬된 경우라면 앞의 원소와 비교하는 연산이 1번 만에 끝나 상수 시간이 되기 때문이다.
'''