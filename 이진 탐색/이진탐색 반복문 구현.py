n, target = map(int, input().split())
array = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("array 안에 원소가 존재하지 않습니다.")
else:
    # 인덱스를 출력하는 것이 아니라 몇 번재 원소인지를 출력하는 것이기 때문에 +1을 해줌
    print(result + 1)
