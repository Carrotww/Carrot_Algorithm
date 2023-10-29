# https://leetcode.com/problems/combinations/

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return list(combinations([x for x in range(1, n+1)], k))


# 내 풀이
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(index, word_list):
            if len(word_list) == k:
                result.append(word_list)
                return
            
            for i in range(index, n+1):
                dfs(i+1, [*word_list, i])
        
        dfs(1, [])
        return result

# dfs풀이
class Solution:
    def combine(self, n:int, k:int) -> List[List[int]]:
        result = []
        
        def dfs(num_list, start, k):
            if k == 0:
                result.append(num_list[:])
                return
            
            for i in range(start, n+1):
                num_list.append(i)
                dfs(num_list, i+1, k-1)
                num_list.pop()
        dfs([], 1, k)
        return result

