from collections import deque
class Solution:
    def solve(self, board):
        q = deque()
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                q.append((0,i))
            if board[len(board)-1][i] == 'O':
                q.append((len(board)-1,i))
        for j in range(1, len(board)-1):
            if board[j][0] == 'O':
                q.append((j,0))
            if board[j][len(board[0])-1] == 'O':
                q.append((j,len(board[0])-1))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            x,y = q.popleft()
            board[x][y] = 'M'
            for d in directions:
                nx,ny = x+d[0],y+d[1]
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] == 'O':
                    q.append((nx,ny))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] =  'X'
                if board[i][j] == 'M':
                    board[i][j] = 'O'