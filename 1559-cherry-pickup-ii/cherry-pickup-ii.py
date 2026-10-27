class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp={}
        def cherry(row,col1,col2):
            if row>=m:
                return 0
            if col1<0 or col1>=n or col2>=n or col2<0:
                return float('-inf')
            state=(row,col1,col2)
            if state in dp:
                return dp[state]
            if col1==col2:
                take1=grid[row][col1]+ cherry(row+1,col1-1,col2-1)
                take2 = grid[row][col1] + cherry(row+1,col1-1,col2)
                take3= grid[row][col1] + cherry(row+1,col1-1,col2+1)
                take4=grid[row][col1] + cherry(row+1,col1,col2-1)
                take5=grid[row][col1] + cherry(row+1,col1,col2)
                take6=grid[row][col1] + cherry(row+1,col1+1,col2)
                take7=grid[row][col1] + cherry(row+1,col1,col2+1)
                take8=grid[row][col1] + cherry(row+1,col1+1,col2+1)
                take9=grid[row][col1] + cherry(row+1,col1+1,col2-1)
            else:
                take1=grid[row][col1]+ grid[row][col2]+ cherry(row+1,col1-1,col2-1)
                take2 = grid[row][col1] + grid[row][col2]+ cherry(row+1,col1-1,col2)
                take3= grid[row][col1] + grid[row][col2]+ cherry(row+1,col1-1,col2+1)
                take4=grid[row][col1] + grid[row][col2]+ cherry(row+1,col1,col2-1)
                take5=grid[row][col1] + grid[row][col2]+ cherry(row+1,col1,col2)
                take6=grid[row][col1] +grid[row][col2]+ cherry(row+1,col1+1,col2)
                take7=grid[row][col1] +grid[row][col2]+ cherry(row+1,col1,col2+1)
                take8=grid[row][col1] +grid[row][col2]+ cherry(row+1,col1+1,col2+1)
                take9=grid[row][col1] +grid[row][col2]+ cherry(row+1,col1+1,col2-1)
            dp[state]= max(take1,take2,take3,take4,take5,take6,take7,take8,take9)
            return dp[state]
        return cherry(0,0,n-1)
            