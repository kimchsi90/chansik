# https://codeup.kr/problem.php?id=6082

num = int(input())
my_list = ['3', '6', '9']
judge = False
for i in range(1, num + 1):
    for j in my_list:
        if j in str(i):
            judge = True
            break
    if judge:
        print('X', end=' ')
    else:
        print(i, end=' ')
    judge = False
