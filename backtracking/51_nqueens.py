class Solution:
    def solveNQueens(self,n):
        def backtrack(row):
            if row == n:
                sol = []
                for r in board:
                    sol.append("".join(r))
                result.append(sol)
                return
            
            for c in range(n):
                if c in col or row+c in pos_diag or row-c in neg_diag:
                    continue 
                # choose
                col.add(c)
                pos_diag.add(row+c)
                neg_diag.add(row-c)
                board[row][c] = "Q"
                # explore
                backtrack(row+1)
                # un choose
                col.remove(c)
                pos_diag.remove(row+c)
                neg_diag.remove(row-c)
                board[row][c] = "."
        result = []
        board = [["."]*n for _ in range(n)]
        col, pos_diag, neg_diag = set(), set(), set()
        backtrack(0)
        return result