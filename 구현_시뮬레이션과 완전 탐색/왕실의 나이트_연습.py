# 행의 위치는 1~8, 열의 위치는 a~h로 표현
# a1과 같이 입력이 주어질 때 나이트가 이동할 수 있는 경우의 수를 print
s = input()

count = 0

x = ord(s[0]) - 96 # ord(a) = 97
y = int(s[1])

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 < nx < 9 and 0 < ny < 9:
        count += 1

print(count)
