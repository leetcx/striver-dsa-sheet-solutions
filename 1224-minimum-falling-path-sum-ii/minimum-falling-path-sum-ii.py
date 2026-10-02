class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)

        dp=[[None]*(n+1) for _ in range(n+1)]

        def calculate(i,j):
            if i==n-1:
                return grid[i][j]

            if dp[i][j] is not None:
                return dp[i][j]

            ans=float('inf')

            for k in range(n):
                if j==k:
                    continue

                ans=min(ans,calculate(i+1,k))

            dp[i][j]=grid[i][j]+ans

            return dp[i][j]

        p=float('inf')

        for i in range(n):
            p=min(p,calculate(0,i))

        return p