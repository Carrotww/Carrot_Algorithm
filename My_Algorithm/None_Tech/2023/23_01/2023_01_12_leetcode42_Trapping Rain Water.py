from typing import List

# stack 풀이
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                before_index = stack.pop()
                
                if not stack:
                    break

                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[before_index]

                result += distance * waters
            stack.append(i)
        return result

# 투 포인터 풀이
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        result = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max <= right_max:
                result += left_max - height[left]
                left += 1
            else:
                result += right_max - height[right]
                right -= 1
        return result