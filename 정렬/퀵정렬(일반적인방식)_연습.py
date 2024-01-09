arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while(left <= right): # 엇갈리기 전까지 계속 진행
        while(left <= end and array[left] <= array[pivot]): # pivot index의 값보다 크거나 같은 값이 나올 때까지 left를 1씩 증가
            left += 1
        while(right > start and array[right] >= array[pivot]): # pivot index의 값보다 작거나 같은 값이 나올 때까지 right를 1씩 감소
            right -= 1
        
        if (left > right): # 엇갈렸다면 작은 값(right)과 pivot의 값을 교체
            array[pivot], array[right] = array[right], array[pivot]
        else: # 엇갈리지 않았다면 left index의 값과 right index의 값을 교체
            array[left], array[right] = array[right], array[left]
    
    # 엇갈린 이후 pivot index의 값과 right(작은 값) index의 값을 바꾸고
    # right(작은 값)을 기준으로 분할됐기 때문에 재귀적으로 반복
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

    return array

print(quick_sort(arr, 0, len(arr) - 1))


'''
퀵정렬의 시간복잡도
평균적으로 Nlog(N)
가로: N, 세로: log2에 N (2등분씩 된다고 가정할 때)
하지만 최악의 경우 O(N**2)의 시간 복잡도를 가짐
리스트가 정렬된 상태일 경우
'''
