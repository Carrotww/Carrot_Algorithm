# https://leetcode.com/problems/largest-number/

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def swap(a, b):
            if str(a) + str(b) < str(b) + str(a):
                return True
            return False

        i = 1
        while i < len(nums):
            j = i
            while j > 0 and swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
        
        return str(int(''.join(map(str, nums))))