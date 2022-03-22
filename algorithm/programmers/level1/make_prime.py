from itertools import combinations

def solution(nums):
    answer = 0
    
    sum_list = list(map(sum, combinations(nums, 3)))
    
    for i in sum_list:
        status = 0
        for j in range(2, i):
            if i % j == 0:
                status = 1
                break
        if status == 0:
            answer += 1

    return answer

print(solution([1, 2, 3, 4]))