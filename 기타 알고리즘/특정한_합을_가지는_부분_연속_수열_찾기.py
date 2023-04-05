n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 4, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 0부터 n-1까지 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    # while 문을 탈출한 상황은 현재의 부분 합이 m 이상이라는 의미
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분 합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
