import enum
from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int): # -> List[int]:
        for i, v in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if (target - v) == nums[j]:
                    return [i, j]

print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))

# [풀이1. 브루트 포스로 계산]===================================================

class Solution1:
    def twoSum(self, nums: List[int], target: int):  # -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution1().twoSum([2, 7, 11, 15], 9))
print(Solution1().twoSum([3, 2, 4], 6))

# [풀이2. in을 이용한 탐색]===================================================

class Solution2:
    def twoSum(self, nums: List[int], target: int):  # -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i + 1:]:
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)


print(Solution2().twoSum([2, 7, 11, 15], 9))
print(Solution2().twoSum([3, 2, 4], 6))

# [풀이3. 첫 번째 수를 뺀 결과 키 조회]===================================================

class Solution3:
    def twoSum(self, nums: List[int], target: int):  # -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
            
        #타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return nums.index(num), nums_map[target-num]


print(Solution3().twoSum([2, 7, 11, 15], 9))
print(Solution3().twoSum([3, 2, 4], 6))

# [풀이4. 조회 구조 개선]===================================================

class Solution4:
    def twoSum(self, nums: List[int], target: int):  # -> List[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i

print(Solution4().twoSum([2, 7, 11, 15], 9))
print(Solution4().twoSum([3, 2, 4], 6))
