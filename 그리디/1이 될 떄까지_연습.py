n, k = map(int, input().split())

count = 0

while True:
    # n이 k로 나눠떨어질 때까지 -1을 뺌
    target = (n // k) * k
    count += n - target
    n = target

    if n < k:
        break
    # n은 이제 k로 나눠 떨어지는 수이기 때문에 k로 1번 나눔
    n /= k
    count += 1

count += n - 1
print(count)
