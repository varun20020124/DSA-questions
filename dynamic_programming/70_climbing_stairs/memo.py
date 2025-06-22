class Solution:
    def climbStairs(self, n):
        memo = [None] * (n+1)
        def rec(i):
            if i>n:
                return 0
            if i == n:
                return 1
            if memo[i]!=None:
                return memo[i]
            memo[i] = rec(i+1) + rec(i+2)
            return memo[i]
        return rec(0)