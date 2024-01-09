def solution(phone_book):
    answer = True
    dict_pb = dict.fromkeys(phone_book, 0)
    
    for nums in phone_book:
        temp = ''
        for num in nums:
            temp += num
            if temp in dict_pb and temp != nums:
                return False
    return answer

print(solution(["119", "97674223", "1195524421"]))


'''
https://school.programmers.co.kr/learn/courses/30/lessons/42577

["119", "97674223", "1195524421"]
false

["123","456","789"]
true

["12","123","1235","567","88"]
false

dict는 내부적으로 해시 테이블(Hash Table)을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 상수 시간에 처리 가능.
temp in dict_pb에서 O(1)의 시간 복잡도를 가지기 때문에 list를 사용할 때(O(N))보다 시간 효율이 좋음.
'''