n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

# INF를 의미하는 10001 값으로 초기화
# 1~m 까지의 범위 표현
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행(바텀업)
d[0] = 0

for i in range(n):  # 화폐 단위
    for j in range(array[i], m + 1):  # 금액
        if d[j - array[i]] != 10001:  # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)


if d[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없을 경우
    print(-1)
else:
    print(d[m])
