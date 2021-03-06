import enum
from typing import *

class Solution:
    def arrayPairSum(self, nums: List[int]):# -> int:
        answer = 0
        nums.sort(reverse=True)
        
        for i in range(1, len(nums), 2):
            answer += nums[i]
        
        return answer
            
print(Solution().arrayPairSum([6, 2, 6, 5, 1, 2]))

# [풀이1. 오름차순 풀이]==========================================================

class Solution1:
    def arrayPairSum(self, nums: List[int]):# -> int:
        sum = 0
        pair = []
        nums.sort()
        
        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        
        return sum
            
print(Solution1().arrayPairSum([6, 2, 6, 5, 1, 2]))

# [풀이2. 짝수 번째 값 계산]==========================================================

class Solution2:
    def arrayPairSum(self, nums: List[int]):# -> int:
        sum = 0
        nums.sort()
        
        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += n
        
        return sum
            
print(Solution2().arrayPairSum([6, 2, 6, 5, 1, 2]))

# [풀이3. 파이썬다운 방식]==========================================================

class Solution3:
    def arrayPairSum(self, nums: List[int]):# -> int:
        return sum(sorted(nums)[::2])
            
print(Solution3().arrayPairSum([6, 2, 6, 5, 1, 2]))