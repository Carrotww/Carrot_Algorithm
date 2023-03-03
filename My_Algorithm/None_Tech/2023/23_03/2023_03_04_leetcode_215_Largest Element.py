# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

from typing import List

# 1번 풀이 - python sort 사용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


# 2번 풀이
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        result = 0
        
        return result