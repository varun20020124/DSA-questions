import heapq
class Solution:
    def maxSlidingWindow(self, nums, k):
        '''
        O(NlogN) : not optimal
        '''
        for i in range(len(nums)):
            nums[i] = -nums[i]
        i,j = 0,k
        res = []
        while j<=len(nums):
            arr = nums[i:j]
            heapq.heapify(arr)
            res.append(-heapq.heappop(arr))
            i+=1
            j+=1
        return res