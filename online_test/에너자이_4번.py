# 1~n 까지 카드, 같은 숫자 무제한 뽑기 가능
# ex. 5를 철수가 3 영희가 2개 뽑았을 때 철수가 3
# 지거나 비기면 -1 출력
def solution(num_cards, num_picked_cards, A_cards):
    sum_a = 0 # 철수의 점수
    sum_b = 0 # 영희의 점수
    num_picked_cards -= num_cards # 영희의 카드 초기화 수 만큼 남은 카드를 뺀다

    for i in range(num_cards - 1, -1, -1): # 카드 역순으로 i = 2, 1, 0
        if num_picked_cards >= A_cards[i]:
            num_picked_cards -= A_cards[i]
            sum_b += i+1
        else:
            sum_a += i+1
 
    return sum_b - sum_a if sum_a < sum_b else -1

'''
테스트 1
입력값 〉
3, 12, [3, 4, 5]
기댓값 〉
4
실행 결과 〉
테스트를 통과하였습니다.
'''