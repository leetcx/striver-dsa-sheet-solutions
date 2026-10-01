class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*(n+1) for _ in range(m+1)]
        def cal(i,j):
            if i>=m or i<0 or j<0 or j>=n or grid[i][j]=="#":
                return float('inf')
            if i==m-1 and j==n-1:
                return grid[m-1][n-1]
            if dp[i][j] != -1:
                return dp[i][j]
            original=grid[i][j]
            grid[i][j]="#"
            right=cal(i,j+1)
            down=cal(i+1,j)
            grid[i][j]=original
            dp[i][j]=grid[i][j] + min(right,down)
            return dp[i][j]
        return cal(0,0)