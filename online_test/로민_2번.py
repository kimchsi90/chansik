# 던진 위치 중심으로 3x3 크기 점수 모두 획득
# 1번만 던짐
# 위치가 주어질 때 점수 출력
# 맞춘 위치가 다트 밖이면 0점

# 맨 위 좌표 (1, 1)

def solution():
    result = 0
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(n)]
    x, y = map(int, input().split())
    if not (1 <= x <= n and 1 <= y <= n):
        return 0

    for i in range(x - 2, x + 1):
        for j in range(y - 2, y + 1):
            if (0 <= i <= n-1 and 0 <= j <= n-1):
                result += scores[i][j]
    return result

print(solution())

'''
6
7 7 6 7 6 1 
2 9 7 9 4 2 
5 4 0 0 7 7 
0 0 6 5 2 6 
4 6 6 3 8 8 
8 6 3 9 6 5 
2 2

'''
