#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# best time to buy and sell stock
# idea 1: brute force
# for each element, find the max profit it can make by selling it
# time complexity: O(n^2)
# space complexity: O(1)
# idea 2: dynamic programming
# for each element, find the max profit it can make by selling it

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_len = len(prices)
        if prices_len < 2:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(1, prices_len):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
# @lc code=end