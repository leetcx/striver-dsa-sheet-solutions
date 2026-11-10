class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        dp={}
        def doit(i, j, grid, health):

            if health <= 0:
                return False

            if i == m-1 and j == n-1:
                return True
            state=(i,j,health)
            if state in dp:
                return dp[state]
            take1 = False
            take2 = False
            take3 = False
            take4 = False

            # Down
            if i+1 < m and grid[i+1][j] != -99:
                ori = grid[i+1][j]
                grid[i+1][j] = -99
                take1 = doit(i+1, j, grid, health-ori)
                grid[i+1][j] = ori

            # Up
            if i-1 >= 0 and grid[i-1][j] != -99:
                ori = grid[i-1][j]
                grid[i-1][j] = -99
                take2 = doit(i-1, j, grid, health-ori)
                grid[i-1][j] = ori

            # Right
            if j+1 < n and grid[i][j+1] != -99:
                ori = grid[i][j+1]
                grid[i][j+1] = -99
                take3 = doit(i, j+1, grid, health-ori)
                grid[i][j+1] = ori

            # Left
            if j-1 >= 0 and grid[i][j-1] != -99:
                ori = grid[i][j-1]
                grid[i][j-1] = -99
                take4 = doit(i, j-1, grid, health-ori)
                grid[i][j-1] = ori

            dp[state]= take1 or take2 or take3 or take4
            return dp[state]

        return doit(0, 0, grid, health-grid[0][0])