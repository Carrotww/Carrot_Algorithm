# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        temp = 1
        for i in range(len(nums)):
            result.append(temp)
            temp *= nums[i]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * temp
            temp *= nums[i]
        
        return result