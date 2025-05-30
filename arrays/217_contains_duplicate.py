class Solution:
    def containsDuplicate(self, nums):
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False