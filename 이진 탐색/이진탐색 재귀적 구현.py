n, target = map(int, input().split())
array = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end: # 찾고자하는 범위에 데이터가 존재하지 않는 것과 동일하므로 None을 return
        return None
    mid = (start + end) // 2 # 중간점 설정
    # 중간 값과 찾고자 하는 값이 동일한 경우(찾고자 하는 값을 찾은 경우) 중간 값의 인덱스를 반환
    if array[mid] == target:
        return mid
    # 중간 값이 찾고자 하는 값보다 작으면 중간 값의 인덱스 + 1부터 끝까지(right_side)를 다시 binary_search로 찾아줌
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    # 중간 값이 찾고자 하는 값보다 크면 시작점부터 중간 값의 인덱스 - 1까지(left_side)를 다시 binary_search로 찾아줌
    else:
        return binary_search(array, target, start, mid-1)

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("array 안에 원소가 존재하지 않습니다.")
else:
    # 인덱스를 출력하는 것이 아니라 몇 번재 원소인지를 출력하는 것이기 때문에 +1을 해줌
    print(result + 1)
