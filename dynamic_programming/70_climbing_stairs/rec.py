class Solution:
    def climbStairs(self, n):
        def rec(i):
            if i>n:
                return 0
            if i==n:
                return 1
            return rec(i+1)+rec(i+2)
        return rec(0)