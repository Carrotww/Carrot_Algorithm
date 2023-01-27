# https://leetcode.com/problems/combinations/

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return list(combinations([x for x in range(1, n+1)], k))

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