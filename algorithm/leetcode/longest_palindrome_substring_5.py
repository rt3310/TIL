from re import M


class Solution:
    def longestPalindrome(self, s: str): # -> str:
        if len(s) < 2:
            return s
        
        counts = []
        for i in range(len(s)):
            left = i
            right = i
            while True:
                if left < 0 or right >= len(s):
                    counts.append([i, left + 1, right - 1])
                    break
                
                if s[left] != s[right]:
                    counts.append([i, left + 1, right - 1])
                    break
                
                left -= 1
                right += 1
        
        i = 0  
        for i in range(len(s)):
            left = i
            right = i + 1
            while True:
                if left < 0 or right >= len(s):
                    counts.append([i, left + 1, right - 1])
                    break

                if s[left] != s[right]:
                    counts.append([i, left + 1, right - 1])
                    break

                left -= 1
                right += 1
        
        maximum = 0
        maxidx = 0
        for i, count in enumerate(counts):
            if count[2] - count[1] > maximum:
                maximum = count[2] - count[1]
                maxidx = i
        
        return s[counts[maxidx][1]:counts[maxidx][2] + 1]

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("ac"))

# [풀이1. 중앙을 중심으로 확장하는 풀이]==========================================================


class Solution1:
    def longestPalindrome(self, s: str):  # -> str:
        def expand(left: int, right: int): # -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
            
        return result
    

print(Solution1().longestPalindrome("babad"))
print(Solution1().longestPalindrome("cbbd"))
print(Solution1().longestPalindrome("ac"))
