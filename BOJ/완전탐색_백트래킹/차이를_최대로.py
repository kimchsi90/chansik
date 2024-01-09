from itertools import permutations

n = int(input()) # 3 <= n <= 8
data = list(map(int, input().split()))
# -100 <= num <= 100

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|의 최댓값
# 원소의 차이가 크게

def calc(array): # O(n)
    result = 0 # O(1)
    n = len(array) # O(1)
    for i in range(n - 1): # O(n - 1)
        result += abs(array[i] - array[i + 1])
    return result

result = 0

for perm in permutations(data): # O(n!)
    result = max(calc(perm), result) # O(n)

print(result)

'''
6
20 1 15 8 4 10

62
'''

# n의 최댓값이 8이므로 순열을 만드는 계산은 약 4만 번이기 때문에 완전탐색으로 해결 가능
# 시간 복잡도: O(n*n!)
# 순열을 만드는 시간 복잡도 n!만큼 반복문을 돌고 매 반복마다 n번 만큼의 계산이 이뤄지므로
# 공간 복잡도: O(n*n! + n)
# data는 n, 순열이 차지하는 공간은 n*n!, 나머지는 변수에 해당하는 1이므로