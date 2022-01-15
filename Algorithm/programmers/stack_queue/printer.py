def solution(priorities, location):
    answer = 0
    
    print_cnt = 0 # 출력한 문서 수
    while(True):
        changed = False # 위치 변경 여부
        
        for i in range(1, len(priorities)): # 중요도 검사
            if priorities[i] > priorities[0]: # 중요도가 높은 문서가 있으면
                priorities.append(priorities.pop(0)) # 뒤로 옮긴다
                changed = True
                break
        if changed == False: # 변경되지 않았다면, 즉 중요도가 높은 문서가 없었다면
            print_cnt += 1
            if location == 0: # 출력 문서가 요청한 문서일 시
                answer = print_cnt
                break
            priorities.pop(0) # 하나를 출력한다

        location = (location + len(priorities) - 1) % len(priorities) # 위치 수정
    
    return answer