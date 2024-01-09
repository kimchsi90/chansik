n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0
count = 0

for i in arr:
    count += 1
    if count >= i: # 처음에는 같은 경우라고 했는데 같거나 현재 그룹의 수가 더 큰 경우로 바꿔야 된다는 것을 알게됨
        result += 1
        count = 0
    
print(result)
