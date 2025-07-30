class Solution:
    def rob(self, nums):
        n = len(nums)
        def rec(i,arr,memo):
            if i >= len(arr):
                return 0
            if memo[i]!=None:
                return memo[i]
            memo[i] = max(arr[i] + rec(i+2,arr,memo),rec(i+1,arr,memo))
            return memo[i]
        if n == 1:
            return nums[0]
        return max(rec(0,nums[1:],[None]*(n-1)),rec(0,nums[:n-1],[None]*(n-1)))