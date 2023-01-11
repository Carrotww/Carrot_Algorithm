from typing import List

# brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            for x in range(i+1, len(nums)):
                if nums[x] == temp:
                    return [i, x]

# in을 이용한 탐색
class Solutiuon:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            
            if temp in nums[i+1:]:
                return [i, nums[i+1:].index(temp) + i + 1]

# 첫 번째 수를 뺀 결과 키 조회