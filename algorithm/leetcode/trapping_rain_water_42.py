from typing import *

# 타임오버 됐다 O(n^2)은 안되는 것 같다.
class Solution:
    def trap(self, height: List[int]): # -> int:
        maxnum = max(height)
        
        water = 0
        for i in range(maxnum, 0, -1):
            idx = -1
            for j in range(len(height)):
                if height[j] >= i:
                    if idx == -1:
                        idx = j
                    else:
                        water += j - idx - 1
                        idx = j
        return water
                
            
print(Solution().trap([2, 1, 2, 3, 4]))

# [풀이1. 투 포인터를 최대로 이동]===================================================

class Solution:
    def trap(self, height: List[int]):  # -> int:
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right],right_max)
            
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# [풀이2. in을 이용한 탐색]===================================================
