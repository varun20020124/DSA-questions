import math
class Solution:
    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        minimum = math.inf
        while low<=high:
            mid = (low+high)//2
            if nums[low] <= nums[mid]:
                minimum = min(minimum,nums[low])
                low = mid + 1
            else:
                minimum = min(minimum, nums[mid])
                high = mid - 1
        return minimum