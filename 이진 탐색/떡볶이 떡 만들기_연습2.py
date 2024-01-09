# 파라메트릭 서치 문제
# 최적화 문제를 예 or 아니오를 결정하는 결정 문제로 바꾸어 해결하는 기법
# 최적화 문제란 어떤 함수의 값을 가능한 낮추거나 최대한 높히는 문제
# 최적화 문제를 바로 해결하기 어려운 경우 그 문제를 여러 번의 결정 문제를 이용해서 문제 형태를 바꿔 해결할 수 있는 형태가 존재
# ex. 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제 -> 탐색 범위를 좁혀가면서 현재 범위에서는 이 조건을 만족하는지 체크해서 그 여부에 따라 탐색 범위를 좁혀가며 가장 알맞은 값을 찾을 수 있음
# 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 '이진 탐색'을 이용하여 해결 가능


# 떡의 개수 n, 요청한 떡의 길이 m
# 적어도 m만큼의 떡을 집에 가져가기 위해 절단기의 최대 높이를 출력
n, m = map(int, input().split())
arr = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2

        total = sum([x - mid for x in arr if x - mid > 0])
        
        if target <= total:
            start = mid + 1
            result = mid

        else:
            end = mid - 1
    
    return result

print(binary_search(arr, m, 0, max(arr)))

'''
4 6
19 15 10 17

15

중간점의 값은 시간이 지날수록 '최적화된 값'이기 되기 때문에 과정을 반복하면서 얻을 수 있는 떡의 길이의 합이
필요한 떡의 길이보다 크거나 같을 때마다 중간점의 값을 기록하면 된다.
'''
