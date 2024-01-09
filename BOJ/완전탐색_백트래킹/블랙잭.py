from itertools import combinations

n, m = map(int, input().split())
# 3 <= n <= 100, 10 <= m <= 300_000
data = list(map(int, input().split()))
# 0 <= num <= 100_000

result = 0

for c in combinations(data, 3): # O(nC3)
    num_sum = sum(c) # O(3)
    if num_sum <= m:
        result = max(result, num_sum) # O(1)

print(result)

'''
5 21
5 6 7 8 9

21
-------------------------------------
10 500
93 181 245 214 315 36 185 138 216 295

497
'''

# 시간 복잡도: O(nC3)
# nC3만큼의 조합을 찾는 연산: n! / ((n-3)!3!), 반복문 내부는 상수 시간
# 공간 복잡도: O(3 * nC3 + n)
# data의 길이 n만큼의 공간, 조합을 저장할 공간 nC3 * 3, 나머지는 변수(n, m, result, c, num_sum)