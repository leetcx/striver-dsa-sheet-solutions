class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        memo = [[-1] * n for _ in range(m)]
        def minpath(grid,row,col):
            if row==m-1 and col==n-1:
                return grid[row][col] 
            if row>=m or col>=n:
                return float("+inf")
            if memo[row][col] != -1:
                return memo[row][col]
            right=minpath(grid,row,col+1)
            left=minpath(grid,row+1,col)
            memo[row][col]=grid[row][col]+min(left,right)
            return memo[row][col]
        return minpath(grid,0,0)
        