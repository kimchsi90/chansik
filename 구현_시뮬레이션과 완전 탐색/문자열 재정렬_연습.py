s = input()

# 모든 알파벳 오름 차순 + 숫자 모두 더해서 뒤에 붙여 출력하기

result = ''
result_num = 0

for i in s:
    if ord('A') <= ord(i) <= ord('Z'):
        result += i
    else:
        result_num += int(i)
print(type(result))
result = sorted(result) # str이 오름차순 정렬된 list로 반환됨
print(type(result))
result = ''.join(result) # 정렬된 list를 str로 변환하기 위해 join을 이용해 list의 원소 사이에 ''를 넣은 str로 변환
print(type(result))

if result_num != 0: # 처음에 풀 때 숫자가 하나라도 존재할 경우를 고려하지 못했음
    result += str(result_num)
print(result)
