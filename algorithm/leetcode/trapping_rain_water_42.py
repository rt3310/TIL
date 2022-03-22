from os import stat
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
                
            
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# [풀이1. 투 포인터를 최대로 이동]===================================================

class Solution1:
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


print(Solution1().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# [풀이2. 스택 쌓기]===================================================

class Solution2:
    def trap(self, height: List[int]):  # -> int:
        stack = []
        volume = 0
        
        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]: # 스택에 값이 있고 현재 블럭이 스택의 마지막 블럭보다 높을 경우
                # 스택에서 꺼낸다
                top = stack.pop()
                
                if not len(stack): # 스택에 값이 없을경우 (?)
                    break
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1 # 현재 위치 - 스택 마지막 값 위치 - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
            
            stack.append(i)
        
        return volume
    
print(Solution2().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
