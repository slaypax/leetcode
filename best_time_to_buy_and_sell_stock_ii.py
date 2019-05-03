# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/
# Runtime: 40 ms, faster than 99.14% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# look at all the numbers and if the day's price is higher than the day before
# the stock went up so you can add the difference to the profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        transaction_day = []
        for i in range(1, len(prices)):
            if prices[i] > prices[i -1]:
                profit += prices[i] - prices[i - 1]
                # to find out what days, if you fancy
                transaction_day.append((i,i - 1))
        return profit