class Solution:
    def threeSum(self, nums):
        triplets = set()
        nums.sort()
        for i in range(len(nums)-2):
            j,k = i+1,len(nums)-1
            while j<k:
                three_sum = nums[i]+nums[j]+nums[k]
                if three_sum > 0:
                    k-=1
                elif three_sum < 0:
                    j+=1
                else:
                    triplets.add((nums[i],nums[j],nums[k]))
                    j+=1
        res = []
        for tup in triplets:
            res.append(list(tup))
        return res