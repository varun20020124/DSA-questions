class Solution:
    def trap(self, height):
        n = len(height)
        lmax, rmax = [0]*n, [0]*n 
        lmax[0] = height[0]
        rmax[n-1] = height[n-1]
        for i in range(1,n):
            lmax[i] = max(height[i],lmax[i-1])
        for j in range(n-2,-1,-1):
            rmax[j] = max(height[j],rmax[j+1])
        area = 0
        for k in range(n):
            area += min(lmax[k],rmax[k]) - height[k]
        return area