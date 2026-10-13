class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp={}
        def ways(i,j):
            if i>=m or j>=n or grid[i][j]==1:
                return 0
            if i== m-1 and j==n-1:
                return 1
            state=(i,j)
            if state in dp:
                return dp[state]
            down=0
            right=0
            down+=ways(i+1,j)
            right+=ways(i,j+1)
            dp[state]= down+right
            return dp[state]
        return ways(0,0)