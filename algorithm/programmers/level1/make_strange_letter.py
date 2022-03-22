def solution(s):
    answer = ''
    
    count = 0
    for v in s:
        if count % 2 == 0:
            answer += v.upper()
        else:
            answer += v.lower()
        count += 1
        
        if v == ' ':
            count = 0
    return answer

print(solution("try hello world"))