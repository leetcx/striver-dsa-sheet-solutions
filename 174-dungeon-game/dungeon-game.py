class Solution:
    def calculateMinimumHP(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        dp=[[None] * (n+1) for _ in range(m+1)]

        def solve(i,j,grid):
            if i>=m or j>=n:
                return float('inf')
            if i==m-1 and j==n-1:
                if grid[i][j]>0:
                    return 1
                else:
                    return abs(grid[i][j]) +1
            if dp[i][j] != None:
                return dp[i][j]
            right=solve(i,j+1,grid)
            down=solve(i+1,j,grid)
            result=min(right,down) - grid[i][j]
            if result<1:
                dp[i][j]= 1
                return 1
            else:
                dp[i][j]= result
                return dp[i][j]
        return solve(0,0,grid)