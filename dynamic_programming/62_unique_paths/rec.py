class Solution:
    def uniquePaths(self,m,n):
        def rec(i,j):
            if i==m-1 or j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            return rec(i+1,j) + rec(i,j+1)
        return rec(0,0)