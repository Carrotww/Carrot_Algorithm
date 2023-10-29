# https://leetcode.com/problems/combination-sum/

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(num_list):
            if sum(num_list) == target:
                temp = sorted(num_list)
                if temp not in result:
                    result.append(temp)
            elif sum(num_list) > target:
                return
            for i in range(len(candidates)):
                num_list.append(candidates[i])
                dfs(num_list)
                num_list.pop()
        dfs([])
        return result