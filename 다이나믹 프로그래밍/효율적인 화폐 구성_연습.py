n, m = map(int, input().split())
# n: 화폐 종류 개수, m: 만들고자하는 수
coins = []
INF = 10001 # 만들 수 없는 값, 특정 금액을 만들 수 있는 화폐 구성이 가능하지 않다는 의미
d = [INF] * (m + 1)
for _ in range(n):
    coins.append(int(input()))

d[0] = 0 # d[j - arr[i]] != INF인 경우를 이용하여 화폐 종류가 1인 값들을 초기화 해주기 위함

# 시간 복잡도는 O(n * m)이며 최대 1,000,000이므로 시간초과 발생하지 않음
for coin in coins: # coin이 바깥 for문인 이유는 안쪽 for문의 시작점을 coin 값으로 정하기 위함
    for i in range(coin, m + 1):
        if d[i - coin] != INF: # i - k를 만드는 방법이 존재할 경우
            d[i] = min(d[i], d[i - coin] + 1)

if d[m] != INF:
    print(d[m])
else:
    print(-1)

'''
2 15
2
3

5
-----
3 4
3
5
7

-1
'''