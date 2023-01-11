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
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            
            if temp in nums[i+1:]:
                return [i, nums[i+1:].index(temp) + i + 1]

# 첫 번째 수를 뺀 결과 키 조회
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i
        
        for i, num in enumerate(nums):
            if target - num in nums_dict and i != nums_dict[target - num]:
                return [i, nums_dict[target - num]]

# 위 풀이 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            if target - num in nums_dict:
                return [i, nums_dict[target-num]]
            nums_dict[num] = i