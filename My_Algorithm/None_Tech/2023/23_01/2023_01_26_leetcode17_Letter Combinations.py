# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_dict = {"1" : "", "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno",
        "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        result = []
        def dfs(index, word):
            if len(word) == len(digits):
                result.append(word)
                return
            
            for i in range(index, len(digits)):
                for char in char_dict[digits[i]]:
                    dfs(i+1, word+char)
        if not digits:
            return []
        dfs(0, "")
        return result