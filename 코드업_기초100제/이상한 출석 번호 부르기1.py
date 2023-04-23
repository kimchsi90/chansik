# https://codeup.kr/problem.php?id=6092

num = int(input())

array = [0] * 24

arr = list(map(int, input().split()))

for i in arr:
    array[i] += 1

for idx, n in enumerate(array):
    if idx == 0:
        continue
    print(n, end=' ')
