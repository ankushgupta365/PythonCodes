class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #one transaction to gain max profit
        l=0
        r=1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(prices[r]-prices[l], maxP)
            else:
                l=r
            r+=1
        return maxP
        