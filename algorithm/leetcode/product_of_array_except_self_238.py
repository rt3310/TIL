from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]): # -> List[int]:
        answer = [1 for _ in range(len(nums))]
        return answer
        
print(Solution().productExceptSelf([1, 2, 3, 4]))

# [풀이1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈]==========================================================

class Solution1:
    def productExceptSelf(self, nums: List[int]): # -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        
        return out
        
print(Solution1().productExceptSelf([1, 2, 3, 4]))

# 0 1 12 123
# 234 34 4   0
# 234 134 124 123