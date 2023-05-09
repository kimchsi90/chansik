for i in range(int(input())):
    # n: 행, m: 렬
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = []
    idx = 0
    for i in range(n):
        dp.append(arr[idx:idx + m])
        idx += m

    for i in range(1, m): # 열
        for j in range(n): # 행
            if j == 0: # 0번째 행일 경우
                dp[j][i] += max(dp[j][i - 1], dp[j + 1][i - 1])
            elif j == n - 1: # 마지막 행일 경우
                dp[j][i] += max(dp[j][i - 1], dp[j - 1][i - 1])
            else: # 중간 행일 경우
                dp[j][i] += max(dp[j][i - 1], dp[j - 1][i - 1], dp[j + 1][i - 1])

    # 마지막 열의 값을 리스트로 만들고 최댓값 출력
    print(max([dp[i][m - 1] for i in range(n)]))


'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

19
16
'''