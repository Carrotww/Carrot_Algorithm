# https://leetcode.com/problems/array-partition/description/
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = sum([nums[x] for x in range(0, len(nums), 2)])
        return result