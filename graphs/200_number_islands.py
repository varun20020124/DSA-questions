from collections import deque
class Solution:
    def numIslands(self, grid):
        def bfs(i,j):
            grid[i][j] == "0"
            q = deque()
            q.append((i,j))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                x,y = q.popleft()
                grid[x][y] = 0
                for d in directions:
                    nx, ny = x+d[0], y+d[1]
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == "1":
                        q.append((nx,ny))
                        grid[nx][ny] = "0"

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i,j)
                    num+=1
        return num