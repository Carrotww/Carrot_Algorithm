from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                top = stack.pop()
                
                if not stack:
                    break
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                result += distance * waters
            stack.append(i)
        
        return result