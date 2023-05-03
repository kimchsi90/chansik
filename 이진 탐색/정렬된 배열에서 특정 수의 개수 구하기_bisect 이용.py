from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

data = list(map(int, input().split()))


def search(data, x):
    count = bisect_right(data, x) - bisect_left(data, x)
    if count == 0:
        return -1
    else:
        return count

# bisect_right: 정렬된 순서를 유지하면서 배열a에 x를 삽입할 가장 오른쪽 인덱스를 반환
# bisect_left: 정렬된 순서를 유지하면서 배열a에 x를 삽입할 가장 왼쪽 인덱스를 반환
print("right: ", bisect_right(data, x))
print("left: ", bisect_left(data, x))
print(search(data, x))

'''
7 2
1 1 2 2 2 2 3

4
'''