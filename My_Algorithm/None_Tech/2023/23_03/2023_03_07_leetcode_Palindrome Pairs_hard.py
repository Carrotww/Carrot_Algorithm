# https://leetcode.com/problems/palindrome-pairs/

from typing import List


# 첫 번째 풀이 - brute force
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def checkpalin(char):
            left, right = 0, len(char)-1
            if len(char) % 2 == 0:
                while right != (len(char) // 2)-1:
                    if char[left] != char[right]:
                        return False
                    left += 1
                    right -= 1
            else:
                while right != (len(char) // 2):
                    if char[left] != char[right]:
                        return False
                    left += 1
                    right -= 1
            return True
        
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if checkpalin(words[i] + words[j]):
                    result.append([i, j])
        
        return result