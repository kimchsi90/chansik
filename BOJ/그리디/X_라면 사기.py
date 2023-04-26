# 아직 못 푼 문제

# 실패 케이스
# 1 2 1 1

# X
# 1 1 1
#   1   1

# O
# 1 1
#   1 1 1

import sys
input = sys.stdin.readline

num_factory = int(input())
arr = list(map(int, input().split()))
pay = 0


def buy_three():
    global pay
    for i in range(num_factory - 2):
        if arr[i+1] > arr[i+2]:
            num_ramen = min(arr[i], arr[i+1] - arr[i+2])
            arr[i+1] -= num_ramen
            arr[i+2] -= num_ramen
            pay += 5 * num_ramen

        if arr[i] and arr[i+1] and arr[i+2] :
            num_ramen = min(arr[i:i+3])
            arr[i] -= num_ramen
            arr[i+1] -= num_ramen
            arr[i+2] -= num_ramen
            pay += 7 * num_ramen


def buy_two():
    global pay
    for i in range(num_factory - 1):
        if arr[i] and arr[i+1]:
            num_ramen = min(arr[i:i+2])
            arr[i] -= num_ramen
            arr[i+1] -= num_ramen
            pay += 5 * num_ramen


def buy_one():
    global pay
    for i in range(num_factory):
        if arr[i]:
            pay += 3 * arr[i]


buy_three()
buy_two()
buy_one()

print(pay)
