class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp={}
        def count(i,j):
            if i>=n or i<0 or j>=m or j<0 :
                return 0
            state=(i,j)
            if state in dp:
                return dp[state]
            take1=0
            take2=0
            take3=0
            take4=0
            if i+1<n and grid[i][j]<grid[i+1][j]:
                take1=count(i+1,j)
            if i-1>=0 and grid[i][j]<grid[i-1][j]:
                take2=count(i-1,j)
            if j+1<m and grid[i][j]<grid[i][j+1]:
                take3=count(i,j+1)
            if j-1>=0 and grid[i][j]<grid[i][j-1]:
                take4=count(i,j-1)
            dp[state]= 1+take1+take2+take3+take4
            return dp[state]
        ans=0
        for i in range(n):
            for j in range(m):
                ans+=count(i,j)
        return ans % ((10**9)+7)

            
                