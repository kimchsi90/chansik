def solution(genres, plays):
    answer = []
    dict_album = {}
    for i in range(len(genres)):
        if not genres[i] in dict_album:
            dict_album[genres[i]] = plays[i]
        else:
            dict_album[genres[i]] += plays[i]

    dict_album = dict(sorted(dict_album.items(), key=lambda item:item[1], reverse=True))

    for key in dict_album.keys():
        list_idx, list_play = [], []
        for i, genre in enumerate(genres):
            if key == genre:
                list_idx.append(i)
                list_play.append(plays[i])
        
        if len(list_idx) == 1: # 장르에 속한 곡이 하나면 하나만 선택
            answer.append(list_idx[0])
        else:
            # 재생횟수 같은 경우 고유 번호 낮은 노래 먼저 수록
            '''
            
            여기서 재생횟수 같은 경우 처리해야함
            
            
            '''
            sorted_play = sorted(list_play, reverse=True)
            answer.append(list_idx[list_play.index(sorted_play[0])])
            answer.append(list_idx[list_play.index(sorted_play[1])])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
 
'''
https://school.programmers.co.kr/learn/courses/30/lessons/42579

["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]
[4, 1, 3, 0]
'''