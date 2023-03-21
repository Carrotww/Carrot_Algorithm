# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x:x[0])

        result.append(intervals[0])
        pre_val = intervals[0][1]

        for i in range(1, len(intervals)):
            if pre_val >= intervals[i][0]:
                if pre_val >= intervals[i][1]:
                    pass
                else:
                    result[-1][1] = intervals[i][1]
                    pre_val = intervals[i][1]
            else:
                result.append(intervals[i])
                pre_val = intervals[i][1]

        return result