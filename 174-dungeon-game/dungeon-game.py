class Solution:
    def calculateMinimumHP(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        dp=[[float('inf')]* (n+1) for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
               
                if i==m-1 and j==n-1:
                    if grid[i][j]>0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=abs(grid[i][j]) +1
                else:   
                    right=dp[i][j+1]
                    down=dp[i+1][j]
                    result=min(right,down) - grid[i][j]
                    if result<1:
                        dp[i][j]= 1
                    
                    else:
                        dp[i][j]= result
                
        return dp[0][0]