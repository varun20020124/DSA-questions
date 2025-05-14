class Solution:
    def isValidSudoku(self, board):
        for i in range(len(board)):
            h,v = set(),set()
            for j in range(len(board)):
                if board[i][j]!=".":
                    if board[i][j] not in h:
                        h.add(board[i][j])
                    else:   return False
                if board[j][i]!=".":
                    if board[j][i] not in v:
                        v.add(board[j][i])
                    else:   return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = set()
                for k in range(3):
                    for l in range(3):
                        square = board[i+k][j+l]
                        if square!=".":
                            if square not in box:
                                box.add(square)
                            else:   return False
        return True