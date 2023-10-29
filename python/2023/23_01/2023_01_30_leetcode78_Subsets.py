# https://leetcode.com/problems/subsets/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(num_list, index):
            result.append(num_list[:])
            
            for i in range(index, len(nums)):
                num_list.append(nums[i])
                dfs(num_list, i+1)
                num_list.pop()
        dfs([], 0)

        # def dfs(index, path):
        #     result.append(path)
        #     for i in range(index, len(nums)):
        #         dfs(i+1, path + [nums[i]])
        # dfs(0, [])
        return result