array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 정렬이 완료된 것이기 때문에 종료
        return
    pivot = start
    left = start + 1
    right = end
    # 엇갈린 경우(left > right일 때) while문 탈출
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[pivot] >= array[left]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈린 경우 작은 데이터(right)와 피벗을 교체
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 엇갈리지 않은 경우 작은 데이터(right)와 큰 데이터(left)를 교
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    # right가 분할의 중심(분할 전 pivot이 자리 이동 후 존재하는 위치)이기 때문에 right를 기준으로 좌/우를 분할
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

'''
시간 복잡도: 평균적으로 O(NlogN)- N(가로: 원소의 개수) * logN(세로: 이상적으로 2분할씩 일어날 경우), 최악의 경우 O(N**2)- 이미 정렬된 경우 앞에서부터 계속 선형 탐색을 해야 하므로.
엄밀히 말하면 pivot을 어떻게 선택하느냐에 따라서 분할이 절반에 가깝게 이루어지지 않고 한쪽에 편향적으로 일어날 경우에 최악의 경우가 일어남

공간 복잡도: O(N)
start, end, pivot, left, right 변수 이외에 array가 N의 길이만큼 공간을 차지하므로
'''