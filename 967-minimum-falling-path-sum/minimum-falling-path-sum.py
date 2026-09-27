class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)
        ans=float('inf')
        memo = [['-inf'] * n for _ in range(n)]
        def falling(grid,row,col):
            nonlocal memo
            if row==n-1 and col<n and col>=0:
                return grid[row][col]
            if row>=n or col<0 or col>=n:
                return float('inf')
            if memo[row][col] != '-inf':
                return memo[row][col]
            down=falling(grid,row+1,col)
            downleft=falling(grid,row+1,col-1)
            downright=falling(grid,row+1,col+1)
            memo[row][col]= grid[row][col]+(min(down,downleft,downright))
            return memo[row][col]
        for i in range(n):
            ans=min(ans,falling(grid,0,i))
        return ans