class Solution:
    def mincost(self,cost):
        n = len(cost)
        if n <= 2:
            return min(cost[0],cost[1])
        # dp[i] represents the min cost to get to index i
        dp = [0] * n
        dp[0],dp[1] = cost[0],cost[1]
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])