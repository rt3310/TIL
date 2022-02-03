from typing import List


class Solution:
    def reverseString(self, s: List[str]):
        s.reverse()
        
Solution.reverseString(Solution, ["h", "e", "l", "l", "o"])

# [풀이1. 투 포인터를 이용한 스왑]===================================================

class Solution1:
    def reverseString(self, s: List[str]):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

Solution1.reverseString(Solution1, ["h", "e", "l", "l", "o"])

# [풀이2. 파이썬다운 방식]===================================================

class Solution2:
    def reverseString(self, s: List[str]):
        s[:] = s[::-1] # 공간 복잡도가 O(1)로 제한되어 있어서 사용한 트릭


Solution2.reverseString(Solution2, ["h", "e", "l", "l", "o"])