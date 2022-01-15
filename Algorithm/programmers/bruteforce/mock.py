def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    hit = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            hit[0] += 1
    
    for i in range(len(answers)):
        if answers[i] == two[i % 8]:
            hit[1] += 1
    
    for i in range(0, len(answers)):
        if answers[i] == three[i % 10]:
            hit[2] += 1
    
    maxnum = max(hit)
    for i in range(len(hit)):
        if hit[i] == maxnum:
            answer.append(i+1)
            
    return answer