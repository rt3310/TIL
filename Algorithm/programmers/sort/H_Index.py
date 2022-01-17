def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)

    print(citations)
    for i, v in enumerate(citations):
        if v >= i + 1:
            answer = i + 1

    return answer

print(solution([3, 0, 6, 1, 5])) # 0 1 3 5 6 