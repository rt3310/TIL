def solution(participant, completion):
    answer = ''
    comple = {} # {완주자:동명이인 인원 수}

    for i in range(len(completion)):
        if comple.get(completion[i]) == None: # 완주 명단 해시에 없으면
            comple[completion[i]] = 1 # 해시 추가
        else:
            comple[completion[i]] += 1 # value값 증가

    for i in range(len(participant)):
        if comple.get(participant[i]) == None or comple.get(participant[i]) == 0: # 완주 명단에 없으면
            answer = participant[i]
            break
        else: # 동명이인이 있을 시
            comple[participant[i]] -= 1 # value값 감소

    return answer
