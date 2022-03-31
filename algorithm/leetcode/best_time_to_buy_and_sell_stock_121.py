from typing import *

from sympy import minpoly

class Solution:
    def maxProfit(self, prices: List[int]): # -> int:
        min_price = max(prices)
        max_benefit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                benefit = prices[i] - min_price
                if benefit > max_benefit:
                    max_benefit = benefit
        
        return max_benefit

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))