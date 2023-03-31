# 행: 1~8
# 열: a~h

user_input = input()
result = 0
x, y = 0, 0

cols = ['a', 'b', 'c', 'd', 'e']
rows = [x+1 for x in range(8)]

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

# 현재 좌표 구하기
for ui in user_input:
    if ui in cols:
        x = user_input.index(ui)
    else:
        y = int(ui)-1

print(x, y)

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if 8 > nx < 0 or 8 > ny < 0:
        continue
    result += 1

print(result)