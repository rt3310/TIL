n = int(input())

max_lead = 0
p1_total = 0
p2_total = 0
result_win = 0
for i in range(n):
    p1, p2 = map(int, input().split())
    p1_total += p1
    p2_total += p2
    
    lead = 0
    win_player = 0
    
    # 총합 비교
    if p1_total > p2_total:
        lead = p1_total - p2_total
        win_player = 1
    else:
        lead = p2_total - p1_total
        win_player = 2
    
    # 이전 max값이랑 비교
    if lead > max_lead:
        max_lead = lead
        result_win = win_player
        
print(result_win, max_lead)