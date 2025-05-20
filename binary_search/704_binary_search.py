class Solution:
    def search(self, num, target):
        low,high = 0,len(num) - 1
        while low<=high:
            mid = (low+high)//2
            if num[mid] == target:
                return mid
            elif num[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1