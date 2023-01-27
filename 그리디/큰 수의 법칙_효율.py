# N: 배열의 크기
# M: 숫자가 더해지는 횟수
# K: 연속해서 K번을 초과하여 더해질 수 없음

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)  # 입력받은 수 정렬

first = data[0]  # 가장 큰 수
second = data[1]  # 두 번째로 큰 수

result = 0
first_count = 0  # 가장 큰 수가 더해지는 횟수
second_count = 0  # 두 번째로 큰 수가 더해지는 횟수
count = 0  # 몇 개의 틀이 더해지는지

# 가장 큰 수가 더해지는 횟수 구하기
# 두 번째로 큰 수는 한 번만 더한다

# K+1이 한개의 틀의 크기, 틀은 반복된다.

count = n // (k + 1)
mod = n % (k + 1)
first_count = count * k
first_count += mod
second_count = count

result = first_count * first + second * second_count

print("result: ", result)
