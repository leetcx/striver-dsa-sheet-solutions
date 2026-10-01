class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        MOD= 10** 9 +7
        dp=[[-1] * (n+1) for _ in range(m+1)]
        def choose(i, j):

            if i<0 or j<0 or i>=m or j>=n:
                return float('inf'),float('-inf')
            if i == m - 1 and j == n - 1:
                return grid[i][j], grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            maxval = float("-inf")
            minval = float("inf")
            if j+1<n:
                rightmin, rightmax = choose(i, j + 1)
                maxval=max(maxval,grid[i][j] * rightmin,grid[i][j] * rightmax)
                minval=min(minval,grid[i][j] * rightmin,grid[i][j] *rightmax)
            if i+1<m:
                downmin, downmax = choose(i + 1, j)
                maxval=max(maxval,grid[i][j] * downmin,grid[i][j] * downmax)
                minval=min(minval,grid[i][j] * downmin,grid[i][j] *downmax)

           

            
            

            dp[i][j]=minval, maxval
            return dp[i][j]

        minval, maxval = choose(0, 0)
        if maxval<0:
            return -1
        return maxval % MOD