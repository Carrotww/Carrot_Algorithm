# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 첫 번째 풀이 시간 하위 5% 너무 오래걸림
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if result >= len(s[i:]):
                break
            index = i
            check_str = set()
            while index < len(s):
                if s[index] in check_str:
                    break
                check_str.add(s[index])
                index += 1
                result = max(result, len(check_str))
        return result

# 책의 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
        
            used[char] = i
        
        return max_length