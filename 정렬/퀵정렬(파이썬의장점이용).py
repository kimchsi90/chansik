array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


array = quick_sort(array)

print(array)

'''
시간 복잡도: 평균적으로 O(NlogN)- N(가로: 원소의 개수) * logN(세로: 이상적으로 2분할씩 일어날 경우), 최악의 경우 O(N**2)- 이미 정렬된 경우 앞에서부터 계속 선형 탐색을 해야 하므로.
엄밀히 말하면 pivot을 어떻게 선택하느냐에 따라서 분할이 절반에 가깝게 이루어지지 않고 한쪽에 편향적으로 일어날 경우에 최악의 경우가 일어남

공간 복잡도: O(N)
array, pivot + tail, left_side + right_side는 총 3N이고 재귀적으로 다시 N에 대해 반복되므로
예를 들어 N이 16개이고 이상적으로 반씩 나눠질 경우 8 + 8, 4 + 4 + 4 + 4, 2 + 2 + 2 + 2 + 2 + 2 + 2, 1 + ... + 1만큼 공간이 필요하여 N * 반복 횟수만큼 스택에 쌓이게 된다. 즉, 입력 값인 N에 비례하기 때문에 O(N)이다.
'''