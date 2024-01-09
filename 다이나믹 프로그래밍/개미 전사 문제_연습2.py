# 식량 창고의 개수 n
n = int(input())
arr = list(map(int, input().split()))

dp = [0] * 100 # i번째 까지의 최적의 해를 저장하는 dp table
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1]) # arr[1]이 아니라!!!!!!!!!!!!!!!!!!! max(arr[0], arr[1])임

for i in range(2, n): # 3 ~ n-1
    # a = dp[i - 2] + arr[i] 
    # b = dp[i - 1]
    # dp[i] = a if a > b else b
    dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])

print(dp[n - 1])


# dp를 사용할 수 있는 조건
# 1. 최적 부분 구조: 특정 i의 최적의 해는 i-1과 i-2 + 현재 값으로 계산할 수 있음
# 큰 문제를 해결하기 위해 작은 문제 2개를 이용하는 것을 확인 할 수 있음
# i-3번째 이하는 앞쪽에서 이미 고려됐기 때문에 고려할 필요가 없음

# 2. 중복되는 부분 문제

'''
4
1 3 1 5

8
'''
