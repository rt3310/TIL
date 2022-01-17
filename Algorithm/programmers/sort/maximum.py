def solution(numbers):
    answer = ''
    
    mul = []
    for v in numbers:
        tmp = []
        for i in range(len(str(v)) - 1, -1, -1):
            tmp.append((v // (10**i)) % 10)
        mul.append(tmp)
    print(sorted(mul, reverse=True))
            
    return answer

print(solution([3, 30, 34, 5, 9]))