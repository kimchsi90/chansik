from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

data = list(map(int, input().split()))


def search(data, x):
    count = bisect_right(data, x) - bisect_left(data, x)
    if count == 0:
        return -1
    else:
        return count


print(search(data, x))
