# https://leetcode.com/problems/permutations/description/

from typing import List

# Permutation 구현해보기
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp_result = []
        
        def dfs(word_list):
            if len(word_list) == 0:
                result.append(temp_result[:])
                return
            for word in word_list:
                next_word_list = word_list[:]
                next_word_list.remove(word)

                temp_result.append(word)
                dfs(next_word_list)
                temp_result.pop()
        dfs(nums)
        
        return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(permutations(nums, len(nums)))