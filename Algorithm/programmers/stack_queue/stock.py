def solution(prices):
    answer = []
    
    for i in range(len(prices)): # 기준 가격
        breaked = 0
        time = 0
        for j in range(i + 1, len(prices)): # 떨어진 상황 체크
            time += 1
            if prices[j] < prices[i]:
                answer.append(time)
                breaked = 1
                break
        if breaked == 0: # 떨어지지 않았을 시
            answer.append(time)
    return answer