"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # palindromic 인지 확인하는 함수
        def checkpalin(word):
            if len(word) == 1:
                return True

            center_index = len(word) // 2
            if len(word) % 2 == 0:
                if word[:center_index] == ''.join(list(reversed(word[center_index:]))):
                    return True
            else:
                if word[:center_index] == ''.join(list(reversed(word[center_index+1:]))):
                    return True
            return False
        
        result = ''
        
        for i in range(len(s)):
            for x in range(len(s), i-1, -1):
                if checkpalin(s[i:x]):
                    result = max(result, s[i:x], key=lambda x: len(x))
                    continue
        
        return result

temp = Solution()
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) == 1 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result

temp = Solution()

# print(temp.longestPalindrome("babad"))
# print(temp.longestPalindrome("bab"))
# print(temp.longestPalindrome("bbbbbaaabbbbb"))
print(temp.longestPalindrome("cbbd"))