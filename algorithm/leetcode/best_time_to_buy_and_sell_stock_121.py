import enum
import sys
from typing import *

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

# [풀이1. 브루트 포스로 계산]==========================================================

class Solution1:
    def maxProfit(self, prices: List[int]): # -> int:
        max_price = 0
        
        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)
        
        return max_price

print(Solution1().maxProfit([7, 1, 5, 3, 6, 4]))

# 시간 초과

# [풀이2. 저점과 현재 값과의 차이 계산]==========================================================

class Solution2:
    def maxProfit(self, prices: List[int]): # -> int:
        profit = 0
        min_price = sys.maxsize
        
        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit

print(Solution2().maxProfit([7, 1, 5, 3, 6, 4]))