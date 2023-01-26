# https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import List

# 내 풀이
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        result = []
        counter_list = [(key, val) for key, val in counter.items()]
        counter_list.sort(key=lambda x:x[1])

        for i in range(k):
            key, val = counter_list.pop()
            result.append(key)
        return result

# Heap 사용
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        counter = Counter(nums)
        heap = result = []
        for c in counter:
            heapq.heappush(heap, (-counter[c], c))
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

# Counter의 most_common 사용
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        return list(zip(*Counter(nums).most_common(k)))[0]