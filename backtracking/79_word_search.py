class Solution:
    def exist(self, board, word):
        def valid(i,j,k):
            return 0<=i<m and 0<=j<n and board[i][j] == word[k]
        def backtrack(i,j,k):
            # base case 
            if len(word) == k:
                return True
            if not valid(i,j,k):
                return False
            temp = board[i][j]
            board[i][j] = "#"
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for d in directions:
                if backtrack(i+d[0],j+d[1],k+1):
                    return True
            board[i][j] = temp 
            return False
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0):
                        return True
        return False