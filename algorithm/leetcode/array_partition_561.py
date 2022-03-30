from typing import *

class Solution:
    def arrayPairSum(self, nums: List[int]):# -> int:
        answer = 0
        nums.sort(reverse=True)
        
        for i in range(1, len(nums), 2):
            answer += nums[i]
        
        return answer
            
print(Solution().arrayPairSum([6, 2, 6, 5, 1, 2]))