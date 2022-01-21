def solution(lottos, win_nums):
    answer = []
    
    hit = 0
    for i in lottos:
        if i != 0:
            if win_nums.count(i) == 1:
                hit += 1
    max_rank = 7 - (hit + lottos.count(0))
    min_rank = 7 - hit
    
    if max_rank >= 6:
        max_rank = 6
        
    if min_rank >= 6:
        min_rank = 6
    
    answer.append(max_rank)
    answer.append(min_rank)
    
    return answer