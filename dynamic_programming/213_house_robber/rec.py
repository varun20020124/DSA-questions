class Solution:
    def rob(self, nums):
        n = len(nums)
        def rec(i,arr):
            if i >= len(arr):
                return 0
            return max(arr[i] + rec(i+2,arr),rec(i+1,arr))
        if n == 1:
            return nums[0]
        return max(rec(0,nums[1:]),rec(0,nums[:n-1]))