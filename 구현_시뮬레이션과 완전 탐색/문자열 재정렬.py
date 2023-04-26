s_arr = list(input())
result = []
value = 0

for i in range(len(s_arr)):
    # if s_arr[i].is_alpha():
    if ord('A') <= ord(s_arr[i]) <= ord('Z'):
        result.append(s_arr[i])
    else:
        value += int(s_arr[i])

# 알파벳 오름차순 정렬
result.sort()

# 숫자가 하나라도 존재하면 append
if value != 0:
    result.append(str(value))
    
print("".join(result))
