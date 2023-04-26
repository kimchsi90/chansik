# 하루는 24 * 60 * 60 = 86,400초 이므로 모든 경우를 다 고려한다고 하더라도 시간 초과되지 않음.(python에서는 1초에 약 2000만번 연산한다고 가정하고 풀면 합리적)
# 완전 탐색 유형

n = int(input())
count = 0

for h in range(n + 1):
    if "3" in str(h):
        count += 60 * 60
        continue
    for m in range(60):
        if "3" in str(m):
            count += 60
            continue
        for s in range(60):
            if "3" in str(s):
                count += 1

print(count)
