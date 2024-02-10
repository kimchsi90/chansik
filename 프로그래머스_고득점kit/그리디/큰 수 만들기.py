def solution(number, k):
    stack = []  # 숫자를 저장할 스택
    for num in number:
        # 스택에 숫자가 있고, k가 0보다 크며, 스택의 마지막 숫자가 현재 숫자보다 작은 경우
        while stack and k > 0 and stack[-1] < num:
            stack.pop()  # 스택의 마지막 숫자 제거
            k -= 1  # 제거 횟수 감소
        stack.append(num)  # 현재 숫자 스택에 추가
    
    # k가 0보다 크면 (제거할 수 있는 기회가 남아있으면) 스택의 끝에서 k개의 숫자 제거
    stack = stack[:-k] if k > 0 else stack
    
    return ''.join(stack)  # 스택에 남은 숫자를 문자열로 변환하여 반환


number = "4177252841"
k = 8

print(solution(number, k))

# https://school.programmers.co.kr/learn/courses/30/lessons/42883