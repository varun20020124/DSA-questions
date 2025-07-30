class Solution:
    def rob(self,nums):
        n = len(nums)
        def rec(i):
            if i >= n:
                return 0
            if memo[i]!=None:
                return memo[i]
            memo[i] = max(nums[i] + rec(i+2), rec(i+1))
            return memo[i]
        memo = [None] * n
        return rec(0)