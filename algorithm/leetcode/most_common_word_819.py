import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]):
        count = {}
        
        paragraph = paragraph.lower()
        paragraph = re.sub("[^a-z0-9]", ' ', paragraph)
        print(paragraph)
        
        para_list = paragraph.split()
        for i in para_list:
            if count.get(i) is None:
                count[i] = 1
            else:
                count[i] += 1
        
        for i in banned:
            if count.get(i) is None:
                continue
            count.pop(i)
        
        return max(count.items(), key=lambda x: x[1])[0]
        
Solution.mostCommonWord(Solution, "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])

# [풀이1. 리스트 컴프리헨션, Counter 객체 사용]==========================================================

class Solution1:
    def mostCommonWord(self, paragraph: str, banned: List[str]):
        words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split()
                if word not in banned]
        
        # counts = collections.defaultdict(int) # defauldict()을 사용해 int 기본값이 자동으로 부여되도록 설정
        counts = collections.Counter(words)
            
        return counts.most_common(1)[0][0] # [('ball', 2)]