# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_pr = 10000
        sell_stock = 0
        for pr in prices:
            if best_pr < pr:
                sell_stock = pr - best_pr
            best_pr = min(best_pr, pr)
        return sell_stock