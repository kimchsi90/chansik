import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
# 4 <= n <= 20
s = [list(map(int, input().split())) for _ in range(n)]
# 1 <= num <= 100

a, b = 0, 0
for c in combinations(range(n), 2):
    for i in range(n):
        for j in range(n):
            if i in c:
                


'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

0
-------------------
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

2
'''