# 투 포인터 알고리즘 사용
n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# 부분합이 m보다 작다면 end += 1
# 부분합이 m보다 크거나 같다면 start += 1

for start in range(n):
    while end < n and interval_sum < m:
        interval_sum += data[end]
        end += 1
    if interval_sum == m: # start를 뺐을 시점에 부분합과 정답이 같을 경우를 체크하기 위해 while문 밖에 있어야 함
        count += 1
    interval_sum -= data[start]

print(count)