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