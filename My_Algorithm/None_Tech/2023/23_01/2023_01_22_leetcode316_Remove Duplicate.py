# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections
        counter = collections.Counter(s)
        stack = []
        
        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            
            while stack and char < stack[-1] and counter[stack[-1]] >= 1:
                stack.pop()
            
            stack.append(char)
        
        return ''.join(stack)