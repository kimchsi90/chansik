# 최대공약수 계산(유클리드 호제법)
# 두 자연수 A, B에 대하여 (A>B일 때) A를 B로 나눈 나머지를 R이라고 하자.
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
# 유클리드 호제법의 아이디어를 그대로 재귀함수로 작성할 수 있다.

# Greatest Common Devisor
def GCD(A, B):
    # if A < B:
    #     A, B = B, A
    R = A % B
    if R == 0:
        return B

    return GCD(B, R)
    

print(GCD(192, 162))