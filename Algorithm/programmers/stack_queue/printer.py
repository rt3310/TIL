def solution(priorities, location):
    answer = 0
    
    print_cnt = 0
    while(True):
        changed = False
        
        for i in range(1, len(priorities)):
            if priorities[i] > priorities[0]:
                priorities.append(priorities.pop(0))
                changed = True
                break
        if changed == False:
            print_cnt += 1
            if location == 0:
                answer = print_cnt
                break
            priorities.pop(0)

        location = (location + len(priorities) - 1) % len(priorities)
    
    return answer

print(solution([4, 2, 3, 1], 2))