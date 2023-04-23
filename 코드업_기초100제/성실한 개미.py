# https://codeup.kr/problem.php?id=6098

import sys
input = sys.stdin.readline
LENGTH = 10
array = []

for i in range(LENGTH):
    array.append(list(map(int, input().split())))

x, y = 1, 1
array[1][1] = 9
while True:
    if array[x][y+1] != 1:
        if array[x][y+1] == 2:
            array[x][y+1] = 9
            break
        if x >= 8 and y >= 8:
            break
        array[x][y+1] = 9
        y += 1
    else:
        if array[x+1][y] == 2:
            array[x+1][y] = 9
            break
        if x >= 8 and y >= 8:
            break
        array[x+1][y] = 9
        x += 1
    

for i in range(LENGTH):
    for j in range(LENGTH):
        print(array[i][j], end=' ')
    print()
