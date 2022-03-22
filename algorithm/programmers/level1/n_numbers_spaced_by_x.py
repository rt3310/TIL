def solution(x, n):
    answer = []
    answer.append(x)
    
    for i in range(n - 1):
        answer.append(answer[len(answer) - 1] + x)
    return answer

print(solution(2, 5))