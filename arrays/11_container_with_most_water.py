class Solution:
    def maxArea(self, heights):
        max_area = 0
        i,j = 0,len(heights)-1
        while i<j:
            area = (j-i) * min(heights[i],heights[j])
            max_area = max(max_area,area)
            if heights[j]<heights[i]:
                j-=1
            else:
                i+=1
        return max_area
        