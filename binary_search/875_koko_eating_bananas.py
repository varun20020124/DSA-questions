import math
class Solution:
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        minimum = max(piles)
        while low<=high:
            mid = (low+high)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time > h:
                low = mid + 1
            else:
                minimum = min(minimum, mid)
                high = mid - 1
        return minimum