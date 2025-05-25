from collections import deque
class Solution:
    def islandsAndTreasures(self, grid):
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visited = [[False]*col for _ in range(row)]
            visited[i][j] = True
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            count = 0
            while q:
                for i in range(len(q)):
                    x,y = q.popleft()
                    if grid[x][y] == 0:
                        return count
                    for d in directions:
                        nx, ny = x+d[0], y+d[1]
                        if 0<=nx<row and 0<=ny<col and visited[nx][ny] == False and grid[nx][ny]!=-1:
                            q.append((nx,ny))
                            visited[nx][ny] = True
                count+=1
            return INF
        INF = 2147483647
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i,j)