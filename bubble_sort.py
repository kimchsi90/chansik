# import unittest

def bubble_sort(data):
    # 처음 생각한 간단한 아이디어
    # for _ in range(len(data) - 1):
    #     for j in range(len(data) - 1):
    #         if data[j] > data[j + 1]:
    #             data[j], data[j + 1] = data[j + 1], data[j]
    
    # 정렬이 완료된 부분을 제외하고 정렬
    for i in range(len(data) - 1, 0, -1): # 9, 8, 7, 6, 5, 4, 3, 2, 1
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


data = [2, 5, 0, 3, 9, 6, 1, 7, 8, 4]

print(bubble_sort(data))

# class unit_test(unittest.TestCase):
#     def test(self):
#         self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort(data))

# 시간 복잡도: O(N**2), 공간 복잡도: O(1)
# 거품 정렬은 별도의 추가 공간을 사용하지 않고 주어진 배열이 차지하고 있는 공간 내에서 값들의 위치만 바꾸기 때문에 O(1)의 공간 복잡도를 가집니다.
# 시간 복잡도는 우선 루프문을 통해 맨 뒤부터 맨 앞까지 모든 인덱스에 접근해야 하기 때문에 기본적으로 O(N)을 시간을 소모하며, 하나의 루프에서는 인접한 값들의 대소 비교 및 자리 교대를 위해서 O(N)을 시간이 필요하게 됩니다. 따라서 거품 정렬은 총 O(N^2)의 시간 복잡도를 가지는 정렬 알고리즘입니다.
# 하지만, 거품 정렬은 부분적으로 정렬되어 있는 배열에 대해서는 최적화를 통해서 성능을 대폭 개선할 수 있으며, 완전히 정렬되어 있는 배열이 들어올 경우, O(N)까지도 시간 복잡도를 향상시킬 수 있습니다.

# https://www.daleseo.com/sort-bubble/ 참고
