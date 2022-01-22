def solution(a, b):
    answer = 0
    
    for i, v in enumerate(a):
        answer += v * b[i]
        
    return answer