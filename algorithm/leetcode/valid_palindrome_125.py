import collections
import re
from typing import Deque

class Solution:
    def isPalindrome(self, s):
        p = re.compile("[a-zA-Z0-9]")
        s = p.findall(s)
        
        if len(s) == 0:
            return True
        
        s = [i.lower() for i in s]
        for i in range(len(s) // 2 + 1):
            if s[i] != s[len(s) - i - 1]:
                return False
        
        return True
        

a = Solution()

print(a.isPalindrome("A man, a plan, a canal: Panama"))

# [풀이1. 리스트로 변환]===================================================

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        
        strs = []
        for char in s:
            if char.isalnum(): # isalnum() 영문자, 숫자 여부를 판별하는 함수
                strs.append(char.lower())
        
        while len(strs) > 1: # 길이가 1이상이면 반복문 실행 -> 0일 경우 체크를 하지 않고 True로 반환 가능
            if strs.pop(0) != strs.pop(): # 양 끝에서 하나씩 빼면서 체크
                return False
            
        return True
    
# [풀이2. 데크 자료형을 이용한 최적화]===================================================

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True

# [풀이3. 슬라이싱 사용]===================================================

class Solution3:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
    
a3 = Solution3()

print(a3.isPalindrome("A man, a plan, a canal: Panama"))
