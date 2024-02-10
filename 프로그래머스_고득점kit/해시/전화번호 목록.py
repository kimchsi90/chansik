def solution(phone_book):
    # 접두어인 경우 false 아니면 true
    phone_book.sort()

    for i, num in enumerate(phone_book):
        for j in range(i + 1, len(phone_book)):
            if num[0] == phone_book[j][0] and len(num) < len(phone_book[j]):
                if num == phone_book[j][:len(num)]:
                    return False
            else:
                break
  
    return True

print(solution(["119", "97674223", "1195524421"]))


# https://school.programmers.co.kr/learn/courses/30/lessons/42577
