def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow - (yellow // 2) + 1): # yellow의 반까지 검사 (1*2와 2*1은 같으므로)
        if yellow % i == 0: # 나눠 떨어지면
            if (2 * (i + yellow // i)) == (brown - 4): # yellow의 둘레와 brown의 꼭짓점을 뺀 변의 길이가 같으면
                answer.append(i + 2)
                answer.append(yellow // i + 2)
                break
    
    answer.sort(reverse=True) # 내림차순 정렬
    return answer