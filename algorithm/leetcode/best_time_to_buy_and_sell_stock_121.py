from typing import *

class Solution:
    def maxProfit(self, prices: List[int]): # -> int:
        answer = 0
        for i in range(len(prices) - 1):
            benefit = max(prices[i+1:]) - prices[i]
            if benefit > answer:
                answer = benefit
        
        return answer

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))