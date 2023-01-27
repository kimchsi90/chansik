# N: 행의 개수, M: 열의 개수, 1~100 자연수
# N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다, 1~10,000 자연수


# # 1. min 사용
# n, m = map(int, input().split())
# result = 0
# for _ in range(n):
#     temp = list(map(int, input().split()))
#     min_value = min(temp)
#     result = max(result, min_value)
#
# print(result)


# 2. 2중 반복문 사용
n, m = map(int, input().split())
result = 0

for _ in range(n):
    datas = list(map(int, input().split()))
    min_value = 10001
    for data in datas:
        min_value = min(min_value, data)
    print(min_value)
    result = max(result, min_value)

print(result)
