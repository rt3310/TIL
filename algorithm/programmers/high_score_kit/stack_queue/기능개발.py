def solution(progresses, speeds):
    answer = []
    days = []
    
    status = 0 # 현재 기준이 되는 일
    count = -1 # answer에 들어간 숫자 개수
    for i in range(len(progresses)):
        days.append(((100 - progresses[i]) // speeds[i]) + (1 if (100 - progresses[i]) % speeds[i] else 0)) # 올림 기능 대신
        
    for i in range(len(days)):
        if days[i] > status: # 기준이 되는 일 보다 크면 기준을 바꾼다.
            status = days[i]
            answer.append(1)
            count = count + 1
        else: # 작으면 해당 일의 배포 개수를 증가시킨다
            answer[count] = answer[count] + 1

    return answer