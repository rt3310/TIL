def solution(N, stages):
    answer = []
    reach = [0 for i in range(N+1)]
    failure = [0 for i in range(N+1)]
    
    for i in stages:
        failure[i - 1] += 1
        for j in range(i):
            reach[j] += 1
    
    failure_rate = []
    for i in range(N):
        tmp = []
        if failure[i] == 0:
            tmp.append(0.0)
        else:
            tmp.append(failure[i] / reach[i])
        tmp.append(i+1)
        failure_rate.append(tmp)
    
    failure_rate = sorted(failure_rate, reverse=True)
    
    for i in failure_rate:
        answer.append(i[1])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))