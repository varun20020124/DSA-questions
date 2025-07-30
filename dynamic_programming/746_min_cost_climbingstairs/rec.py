class Solution:
    def mincost(self,cost):
        n = len(cost)
        def rec(i):
            if i>=n:
                return 0
            return cost[i] + min(rec(i+1),rec(i+2))
        return min(rec(0),rec(1))