n = int(input())

coins = [500, 100, 50, 10]

count = 0

# for coin in coins:
#     div, mod = divmod(n, coin)
#     count += div
#     n = mod
#     if n == 0:
#         break

# print(count)

for coin in coins:
    count += n//coin
    n %= coin

print(count)

'''
화폐의 종류를 K라고 할 때 알고리즘의 시간 복잡도는 O(K)이다.
돈의 액수와 상관없이 화폐의 종류 수에 따라 시간 복잡도가 결정된다.

공간 복잡도는 
'''