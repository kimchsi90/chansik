# 피보나치 수열
# f(1), f(2) = 1, 1
# f3 2 f4 3 f5 5


def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)


print(fibo(5))


'''
재귀적으로 피보나치 수열을 구현할 경우 시간복잡도는 O(2**n)이다.
f(30)을 계산하기 위해 10억 가량의 연산을 수행해야 한다.


'''