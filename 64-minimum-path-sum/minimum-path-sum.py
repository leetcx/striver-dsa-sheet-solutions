class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1] * (n+1) for _ in range(m+1)]
        def cal(i,j):
            
            if i==m-1 and j==n-1:
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            downsum=float('inf')
            rightsum=float('inf')
            if i+1<m :
                downsum=grid[i][j]+cal(i+1,j)
            if j+1<n:
                rightsum=grid[i][j]+cal(i,j+1)
            dp[i][j]= min(downsum,rightsum)
            return dp[i][j]
        return cal(0,0)
            