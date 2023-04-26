arr = list(map(int, input()))
result = arr[0]

for i in range(1, len(arr)):
    # 둘 중 하나라도 0 또는 1이면 더하기
    if result <= 1 or arr[i] <= 1:
        result += arr[i]
    else:
        result *= arr[i]

print(result)