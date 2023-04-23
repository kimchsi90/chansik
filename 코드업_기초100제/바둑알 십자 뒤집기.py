# https://codeup.kr/problem.php?id=6096

import sys
input = sys.stdin.readline
LENGTH = 19

array = []
for _ in range(LENGTH):
    array.append(list(map(int, input().split())))

num = int(input())

for _ in range(num):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(LENGTH):
        for j in range(LENGTH):
            if x == i:
                if array[i][j] == 1:
                    array[i][j] = 0
                else:
                    array[i][j] = 1
            if y == j:
                if array[i][j] == 1:
                    array[i][j] = 0
                else:
                    array[i][j] = 1

for i in range(LENGTH):
    for j in range(LENGTH):
        print(array[i][j], end=' ')
    print()
