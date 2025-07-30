class Solution:
    def rob(self,nums):
        n = len(nums)
        def rec(i):
            if i >= n:
                return 0
            return max(nums[i] + rec(i+2), rec(i+1))
        return rec(0)