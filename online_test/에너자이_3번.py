def solution(n, coins):
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(min(coins), n + 1):
        for coin in coins:
            idx = i - coin
            if idx < 0:
                continue
            if dp[idx]:
                dp[i] = True

    return 1 if dp[i] else 0


print(solution(11, [3, 5]))

'''
테스트 1
입력값 〉
11, [3, 5]
기댓값 〉 1

테스트 2
입력값 〉
11, [3, 7]
기댓값 〉 0
'''