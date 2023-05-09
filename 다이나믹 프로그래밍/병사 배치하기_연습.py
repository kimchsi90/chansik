n = int(input())
arr = list(map(int, input().split()))
# 가장 긴 증가하는 부분 수열 문제로 치환하기 위해 리스트 역순으로 변환
arr.reverse()
dp = [1] * n # 원소가 1개일 때를 생각하여 dp table의 값을 1로 초기화

# 가장 긴 증가하는 부분 수열 알고리즘
# 해당 i를 마지막 원소로 가진 부분 수열의 길이를 dp[i]에 넣기
for i in range(1, n): # 1번째부터 n - 1까지
    for j in range(0, i): # 지금 값을 정하고자 하는 i값의 바로 앞 인덱스인 i - 1 까지의 모든 원소를 확인
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외 시켜야하는 병사의 최소 수 출력
print(n - max(dp))

'''
7
15 11 4 8 5 2 4

2
'''