class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        # cycle check
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        # locating cycle
        fast = nums[0]
        while fast!=slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
        