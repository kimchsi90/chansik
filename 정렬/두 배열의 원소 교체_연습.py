n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 배열 a, b는 n개의 자연수 원소를 가지고 있음
# 최대 K번의 a와 b의 원소를 바꿔치기 가능
# 최종 목표는 배열 a의 합이 최대가 되는 것
# n, k, a, b가 주어졌을 때 최대 k번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 a의 최댓값 출력

# 1 <= n <= 100,000 원소의 최대 개수는 10만개기 때문에 O(N**2) 시간복잡도를 가지는 정렬 알고리즘을 사용할 경우 시간 초과 판정
# 최악의 경우에도 O(NlogN)을 보장하는 정렬 알고리즘을 이용할 필요가 있음

a.sort() # 오름차순(작은것부터 커짐)
b.sort(reverse=True) # 내림차순(큰것부터 작아짐)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

'''
5 3
1 2 5 4 3
5 5 6 6 5

26
'''
