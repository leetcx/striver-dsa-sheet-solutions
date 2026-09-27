class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        memo = [[-1] * n for _ in range(m)]
        def unique(grid,row,col):
            nonlocal count
            moved=False
            nonlocal memo
           
            if row>=m or row<0 or col<0 or col>=n:
                return 0
            if grid[row][col]==1:
                return 0
            if row==m-1 and col==n-1:
                return 1
            
            
            if memo[row][col] != -1:
                return memo[row][col]
            right=   unique(grid,row,col+1)
                
            down= unique(grid,row+1,col)
                
            memo[row][col]=right+down
            return right+down
        if grid[0][0]==1:
            return 0
        return unique(grid,0,0)
        
         
            
            
            