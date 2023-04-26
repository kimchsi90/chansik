# 공포도 X면 X명 이상으로 구성한 그룹에 참여
# 최대 그룹의 수 출력
# 모든 모험가가 여행에 참여해야 한다는 말이 없으므로 참여하지 않는 모험가도 있을 수 있음

# 현재 그룹에 포함된 모험가의 수 >= 현재 확인하고 있는 모험가의 공포도

n = int(input())
arr = list(map(int, input().split()))
result = 0
arr.sort()
num_mem = 0

for i in arr:
    num_mem += 1
    if i >= num_mem:
        result += 1
        num_mem = 0

print(result)
   