class Solution:
    def maxProfit(self, prices):
        i,j = 0,1
        max_profit = 0
        while j<len(prices):
            profit = prices[j]-prices[i]
            if profit <= 0:
                i = j
                j+=1
            else:
                max_profit = max(max_profit,profit)
                j+=1
        return max_profit