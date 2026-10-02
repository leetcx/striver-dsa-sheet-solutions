class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)

        dp=[[0]*n for _ in range(n)]

        for j in range(n):
            dp[n-1][j]=grid[n-1][j]

        for i in range(n-2,-1,-1):
            for j in range(n):
                ans=float('inf')

                for k in range(n):
                    if j==k:
                        continue

                    ans=min(ans,dp[i+1][k])

                dp[i][j]=grid[i][j]+ans

        ans=float('inf')

        for j in range(n):
            ans=min(ans,dp[0][j])

        return ans