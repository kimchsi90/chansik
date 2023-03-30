n, m = map(int, input().split())
array = list(map(int, input().split()))


def get_result(target, array):
    result = 0
    for data in array:
        if data - target > 0:
            result += data - target
    return result


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2  # mid는 자르는 높이
        # 떡의 양이 충분한 경우 줄여야 하므로 오른쪽 탐색
        if get_result(mid, array) >= target:
            start = mid + 1
            answer = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기서 값 기록. 반복을 계속할 수록 최적화된 값이 된다.
        # 떡의 양이 부족한 경우 높여야 하므로 왼쪽 탐색
        else:
            end = mid - 1
    return answer


print(binary_search(array, m, 0, max(array)))
