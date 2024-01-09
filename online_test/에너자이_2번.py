from itertools import combinations

def calculate_probability(p, n, a, b):
    # A팀이 추가로 이길 횟수
    additional_wins_needed = n - a

    # 가능한 모든 경기 조합을 생성
    total_games = additional_wins_needed + (n-b-1)
    game_combinations = list(combinations(range(total_games), additional_wins_needed))
    print(game_combinations)


    # nums = [1,2,3,4]
    # combi = list(combinations(nums, 2))

    # 각 조합에 대해 확률을 계산하고 합산
    total_probability = 0
    for combination in game_combinations:
        probability = (p ** additional_wins_needed) * ((1 - p) ** b)
        total_probability += probability

    return total_probability * 10000

# A팀이 이길 확률은 0.7
p = 0.7

# 총 7번 이겨야 함
n = 7

# A팀은 이미 2번 이김
a = 2

# B팀은 이미 5번 이김
b = 5

# A팀이 우승할 확률을 계산
probability = calculate_probability(p, n, a, b)
print(f"A팀이 우승할 확률: {probability}")


# 4201

'''
테스트 1
입력값 5, 0.5, 4, 2
기댓값 〉 8750

테스트 2
입력값 〉 7, 0.7, 2, 5
기댓값 〉 4201
'''