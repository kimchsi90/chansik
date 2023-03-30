for _ in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index : index + m])
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = array[i][j] + dp[i - 1][j]
            # 왼쪽에서 오는 경우
            left = array[i][j] + dp[i][j]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = array[i][j] + dp[i + 1][j]
            dp[i][j] = max(left_up, left, left_down)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
