class Solution:
    def rob(self, nums):
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        def tab(arr):
            dp = [0]*(len(arr))
            if len(arr) == 2: return max(arr[0],arr[1])
            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])
            for i in range(2,len(arr)):
                dp[i] = max(arr[i]+dp[i-2],dp[i-1])
            return dp[-1]
        return max(tab(nums[1:]),tab(nums[:n-1]))
        