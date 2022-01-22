def solution(numbers):
    answer = ''
    
    string = list(map(str, numbers))
    mul = []
    result = []
    for i, v in enumerate(string):
        tmp = []
        tmp.append(v + (v[0] * (4 - len(v))))
        tmp.append(len(v))
        mul.append(tmp)

    mul.sort(reverse=True)
    for i in mul:
        result.append(i[0][:i[1]])
    
    answer = ''.join(result)
    
    return answer

print(solution([3, 30, 34, 5, 9]))
# 반례
print(solution([20, 201, 41])) # 200000 201111 411111
# 4120120 -> 4120201
print(solution([60, 605, 81, 604, 59])) # 202222 210222
# 454444 449444
print(solution([0, 0, 0, 0]))