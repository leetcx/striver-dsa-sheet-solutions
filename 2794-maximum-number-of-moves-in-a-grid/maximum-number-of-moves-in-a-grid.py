class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp={}
        def count(i,j):
            if i>=m or i<0 or j<0 or j>=n:
                return 0
            state=(i,j)
            if state in dp:
                return dp[state]
            move1=0
            move2=0
            move3=0
            if i-1>=0 and j+1<n and grid[i][j]<grid[i-1][j+1]:
                move1=1+count(i-1,j+1)
            if j+1<n and grid[i][j]<grid[i][j+1]:
                move2=1+count(i,j+1)
            if i+1<m and j+1<n and grid[i][j]<grid[i+1][j+1]:
                move3=1+count(i+1,j+1)
            dp[state]= max(move1,move2,move3)
            return dp[state]
        ans=float('-inf')
        for i in range(m):
            ans=max(ans,count(i,0))
        return ans

