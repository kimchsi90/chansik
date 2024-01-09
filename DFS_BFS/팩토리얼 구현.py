# n! = 1 * 2 * ... * (n-1) * (n)
# 수학적으로 0!과 1!은 1이다.

# 반복적으로 구현한 n!
def factofial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1) # 수학적으로 정의된 점화식을 그대로 이용한다는 점에서 반복문을 이용할 때보다 코드가 간결하고 직관적


print('반복적으로 구현: ', factofial_iterative(5))
print('재귀적으로 구현: ', factorial_recursive(5))
