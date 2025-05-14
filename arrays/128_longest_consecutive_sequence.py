class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        nums = set(nums)
        for num in nums:
            if (num-1) not in nums:
                count = 0
                while num + count in nums:
                    count+=1
                    longest = max(longest, count)
        return longest