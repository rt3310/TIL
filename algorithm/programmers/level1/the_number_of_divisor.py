from math import ceil, floor, sqrt
from operator import le
from typing import List

def solution(left, right):
    answer = 0
    
    if left == 1:
        answer -= 1
        left = 2
    
    while left <= right:
        if sqrt(left) == floor(sqrt(left)):
            answer -= left
        else:
            answer += left
        left += 1
    return answer

print(solution(1, 2))