import imp
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]):
        lets = []
        digs = []
        
        for i in logs:
            if i.split()[1].isdigit():
                digs.append(i)
            else:
                lets.append(i)
                
        lets.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return lets + digs
            
        
Solution.reorderLogFiles(Solution, ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])

# [풀이1. 람다와 + 연산자를 이용]===========================================
class Solution:
    def reorderLogFiles(self, logs: List[str]):
        letters, digits = [], []
        
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits