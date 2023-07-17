# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import defaultdict
        jewels_dict = defaultdict(int)
        result = 0
        
        for jewels in jewels:
            jewels_dict[jewels] += 1
        
        for stone in stones:
            if stone in jewels_dict:
                result += 1
        
        return result

# counter 사용
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        from collections import Counter
        counter = Counter(stones)
        for jewel in jewels:
            result += counter[jewel]
        
        return result

# 한줄 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)