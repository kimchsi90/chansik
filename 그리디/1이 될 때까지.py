# n, k가 100,000 이하의 정수이기 때문에 n이 k로 나누어떨어지면 나누고 아니면 1을 빼는 방식으로 간단하게 해도 됨.
# 하지만 이 방법으로 하게되면 반복문을 한 번 거치면 무조건 n을 k로 나누기 때문에 기하급수적으로 값이 줄어듦(logN의 시간 복잡도). n과 k가 백억, 천억이 넘어가는 매우 큰 수라도 logN의 시간 복잡도로 빠르게 문제를 해결할 수 있음.
n, k = map(int, input().split())
count = 0

while True:
    target = (n//k) * k
    count += (n - target)
    n = target
    
    if k > n:
        break
    
    count += 1
    n //= k

count += (n - 1)
print(count)
