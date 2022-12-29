# https://leetcode.com/problems/reorder-data-in-log-files/submissions/

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha_list, num_list = [], []
        for i in range(len(logs)):
            temp = logs[i]
            if temp.split()[1].isalpha():
                alpha_list.append(temp)
                continue
            num_list.append((temp, i))
        result_alpha = []
        if alpha_list:
            for alpha in alpha_list:
                temp = alpha.split(maxsplit=1)
                result_alpha.append((temp[0], temp[1]))
        result_alpha.sort(key=lambda x: (x[1], x[0]))
        num_list.sort(key=lambda x:x[1])
        result = []
        for i in result_alpha:
            result.append(' '.join(i))
        for i in num_list:
            result.append(i[0])
        return result
        

print(Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))