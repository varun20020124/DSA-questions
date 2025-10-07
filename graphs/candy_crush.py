def candy_crush(grid):
    m,n = len(grid), len(grid[0])
    def mark():
        flag = False
        for i in range(m):
            for j in range(n-2):
                flag = True
                if abs(grid[i][j])!=0 and abs(grid[i][j])==abs(grid[i][j+1])==abs(grid[i][j+2]):
                    grid[i][j] = -abs(grid[i][j])
                    grid[i][j+1] = -abs(grid[i][j+1])
                    grid[i][j+2] = -abs(grid[i][j+2])
        for j in range(n):
            for i in range(m-2):
                flag = True
                if abs(grid[i][j])!=0 and abs(grid[i][j])==abs(grid[i+1][j])==abs(grid[i+2][j]):
                    grid[i][j] = -abs(grid[i][j])
                    grid[i+1][j] = -abs(grid[i+1][j])
                    grid[i+2][j] = -abs(grid[i+2][j])
        return flag
    def move_down():
        for j in range(n):
            stack = []
            for i in range(m-1,-1,-1):
                if grid[i][j] > 0:
                    stack.append(grid[i][j])
            for i in range(m-1,-1,-1):
                if stack:
                    grid[i][j] = stack.pop()
                else:
                    grid[i][j] = 0
        pass
    while True:
        if not mark():
            break
        move_down()
    return grid    