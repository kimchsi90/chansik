# O(N)의 시간 복잡도로 string 뒤집기

def solution(string):
    # 맨 처음 생각한 간단한 방법
    # new_s = ""
    # for i in range(len(string) - 1, -1, -1): # O(N)
    #     new_s += string[i]
    # return new_s

    # 개선된 방법
    n = len(string)
    string = list(string)
    for i in range(n // 2): # O(N//2)
        string[i], string[n - i - 1] = string[n - i - 1], string[i]

    return ''.join(string)

my_string = "abcdefghijklmnopqrstuvwxyz"
print(solution(my_string))

# 시간 복잡도: O(N), 공간 복잡도: O(1)