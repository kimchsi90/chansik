import math

user_input = input()

my_list = user_input.split(' ')

curr_plan = int(my_list[0])
usage = int(my_list[1])
rate_plan = {29900: 300, 34900: 1000,
             39900: 2000, 49900: 6000, 59900: 11000, 69900: math.inf}


def better_curr_plan(rate_plan, usage):
    rate = list(rate_plan.keys())
    data = list(rate_plan.values())
    data_range = []
    # Mutable sort. 작은 순 -> 큰 순으로 정렬.
    rate.sort()

    for i in range(len(rate)-1):
        excess_data = (rate[i+1] - rate[i]) / 20
        data_range.append(data[i] + excess_data)

    for i in range(len(data_range)):
        if usage <= data_range[i]:
            return rate[i]

    return rate[-1]


def rate_calc(rate_plan, curr_plan, usage):

    if curr_plan == 69900:
        return 69900

    data_limit = rate_plan[curr_plan]

    if usage <= data_limit:
        return curr_plan

    excess = usage - data_limit

    if (excess >= 1250) and (excess < 5000):
        return curr_plan + 25000
    else:
        return curr_plan + min([20 * excess, 180000])


better_plan = better_curr_plan(rate_plan, usage)
print(better_plan, end=" ")
print(rate_calc(rate_plan, curr_plan, usage), end=" ")
print(rate_calc(rate_plan, better_plan, usage))

# 데이터 사용량 줄이지 않고 요금 줄이기

# 사용량 n
# plan

'''
출력
추천요금제, 현재 요금제로 사용시 월 요금, 추천요금제 사용시 월 요금

최대 18만원임

'''