# 전형적인 시뮬레이션, 완전탐색 문제 유형이면서도 2차원 좌표를 이용한 구현 문제라고 할 수 있음

LENGTH = 8
count = 0
arr = [[0] * (LENGTH + 1) for _ in range(LENGTH + 1)]
transform = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
user_input = input()
x, y = user_input[0], int(user_input[1])
x = transform.index(x) + 1
# 문자를 유니코드 숫자로 변환하여 x를 숫자 좌표로 바꿈
# x = int(ord(x)) - int(ord('a')) + 1

# 상좌/상우/좌상/좌하/우상/우하/하좌/하우
dx = [2, 2, 1, -1, 1, -1, -2, -2] # 행
dy = [-1, 1, -2, -2, 2, 2, -1, -1] # 열
# steps = [(2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2), (-2, -1), (-2, -1)]

# for step in steps:
#    nx = x + step[0]
#    ny = x + step[1]
#    ...

for i in range(LENGTH):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)
