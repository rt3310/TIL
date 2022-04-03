from re import L
from typing import *

class Solution:
    def threeSum(self, nums: List[int]): # -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        answer = []
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        pivot = 1
        while pivot < len(nums) - 1:
            total = nums[left] + nums[pivot] + nums[right]
            
            
            if total == 0:
                if answer.count([nums[left], nums[pivot], nums[right]]) == 0:
                    answer.append([nums[left], nums[pivot], nums[right]])
                left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1
                
            if left >= pivot or right <= pivot:
                left = 0
                right = len(nums) - 1
                pivot += 1
        
        return answer
    
print(Solution().threeSum([-1,0,1,2,-1,-4]))

# [풀이1. 브루트 포스로 계산]==========================================================
class Solution1:
    def threeSum(self, nums: List[int]): # -> List[List[int]]:
        results = []
        nums.sort()
        
        # 브루트 포스 n^3 반복
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j < i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k < j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append((nums[i], nums[j], nums[k]))
        
        return results

print(Solution1().threeSum([-1,0,1,2,-1,-4]))
# 시간초과

# [풀이2. 투 포인터로 합 계산]==========================================================
class Solution2:
    def threeSum(self, nums: List[int]): # -> List[List[int]]:
        results = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i < 0 and nums[i] == nums[i - 1]:
                continue
            
            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0인 경우이므로 정답 및 스킵처리
                    results.append((nums[i], nums[left], nums[right]))
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right += 1
                    
                    left += 1
                    right -= 1
    
        return results

print(Solution2().threeSum([-1,0,1,2,-1,-4]))