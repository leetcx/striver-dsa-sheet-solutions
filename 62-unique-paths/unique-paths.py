class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1] * (n+1) for _ in range(m+1)]
        def move(i,j):
            if i==m-1 and j==n-1:
                return 1
            
            if i>= m or j>=n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            a=move(i+1,j)
            b=move(i,j+1)
            total=a+b
            dp[i][j]=total
            return total
        return move(0,0)