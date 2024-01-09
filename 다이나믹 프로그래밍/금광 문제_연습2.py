# 테스트 케이스 1 <= t <= 1000
for _ in range(int(input())):
    n, m = map(int, input().split()) # 1 <= n행, m열 <= 20
    data = list(map(int, input().split())) # 1차원 리스트(2차원 dp 테이블로 변환 필요)
    dp = []

    # for i in range(n):
    #     temp = []
    #     for j in range(m):
    #         temp.append(data[m * i + j])
    #     dp.append(temp)
    # 리스트를 이차원 리스트로 바꿀 경우 아래와 같이 간단하게 구현 가능
    
    for i in range(n):
        dp.append(data[i * m : (i + 1) * m])

    for y in range(1, m): # 1열부터 m-1열까지
        for x in range(n): # 0행부터 n-1행까지
            left = dp[x][y - 1]
            if x == 0: # 맨 윗 행일 때
                left_up = 0
            else:
                left_up = dp[x - 1][y - 1]
            if x == n - 1: # 맨 밑 행일 때
                left_down = 0
            else:
                left_down = dp[x + 1][y - 1]

            dp[x][y] = max(left_up, left, left_down) + dp[x][y]
    
    result = max([dp[x][m - 1] for x in range(n)])
    print(result)

    '''
    맨 마지막 열의 최댓값을 찾는 방법 2번째
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    '''


'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

19
16

dp 테이블을 따로 만들지 않고 주어진 값을 그대로 사용해서 해결 가능.

'''