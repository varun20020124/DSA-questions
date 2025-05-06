class Solution:
    def productExceptSelf(self, nums):
        l,r = 1,1
        lprod, rprod = [],[]
        for i in range(len(nums)):
            lprod.append(l)
            l *= nums[i]
            
        for j in range(len(nums)-1,-1,-1):
            rprod.append(r)
            r *= nums[j]
        
        prod = []
        for k in range(len(nums)):
            prod.append(lprod[k] * rprod[::-1][k])
        return prod