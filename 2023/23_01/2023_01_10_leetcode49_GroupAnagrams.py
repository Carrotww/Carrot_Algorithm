from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)
        for i in strs:
            word = ''.join(sorted(i))
            sorted_words[word].append(i)

        result = [sorted(x) for x in sorted_words.values()]
        result.sort(key=lambda x: len(x))
        
        return result

temp = Solution()

print(temp.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))