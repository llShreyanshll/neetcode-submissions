class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 0
        while l <= r and r < len(prices):
            curr = prices[r] - prices[l]
            profit = max(curr, profit)

            if prices[r] < prices [l]:
                l = r

            r+=1
            


        return profit

