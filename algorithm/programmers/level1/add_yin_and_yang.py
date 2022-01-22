def solution(absolutes, signs):
    answer = 0
    
    for i, v in enumerate(absolutes):
        if signs[i] == True:
            answer += v
        else:
            answer += v * -1
    return answer