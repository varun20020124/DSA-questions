class Solution:
    def mincost(self,cost):
        n = len(cost)
        def rec(i):
            if i>=n:
                return 0
            if memo[i]!=None:
                return memo[i]
            memo[i] = cost[i] + min(rec(i+1),rec(i+2))
            return memo[i]
        memo = [None] * n
        return min(rec(0),rec(1))