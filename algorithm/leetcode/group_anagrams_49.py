from typing import *
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]): # -> List[List[str]]:
        strs_list = []
        for str in strs:
            tmp = []
            for i in str:
                tmp.append(i)
            tmp.sort()
            tmp = ''.join(tmp)
            strs_list.append(tmp)
        str_dict = collections.defaultdict(list)
        for i, str in enumerate(strs_list):
            str_dict[str].append(strs[i])
        return list(str_dict.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs=strs))

# [풀이1. 정렬하여 딕셔너리에 추가]==========================================================


class Solution1:
    def groupAnagrams(self, strs: List[str]):  # -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()
    

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution1().groupAnagrams(strs=strs))
