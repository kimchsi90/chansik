n = int(input()) # 0 ~ 23

count = 0
# 00:00:00 ~ n:59:59 중 3이 들어간 경우 count하기
# 24 * 60 * 60 = 86,400번 for문을 도는데 python을 이용했을 때 1초에 2000만 번 이상의 연산이 가능하기 때문에
# 따라서 단순히 1씩 증가시켜 3이 들어갔는지 확인하면 됨(컴퓨터 입장에서 그다지 많은 경우의 수가 아닌 것)
# 완전 탐색(brute forcing) 문제 유형

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
