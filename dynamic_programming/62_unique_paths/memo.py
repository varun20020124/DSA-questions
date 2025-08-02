class Solution:
    def uniquePaths(self,m,n):
        def rec(i,j):
            if i==m-1 or j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if memo[i][j]!=None:
                return memo[i][j]
            memo[i][j] = rec(i+1,j) + rec(i,j+1)
            return memo[i][j]
        memo = [[None]*n for _ in range(m)]
        return rec(0,0)