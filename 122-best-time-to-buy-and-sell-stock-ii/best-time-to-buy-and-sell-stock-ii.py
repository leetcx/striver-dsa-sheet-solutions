class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1] * 3 for _ in range(n+1)]
        k=2
        for i in range(3):
            dp[n][i]=0
        for i in range(n-1,-1,-1):
            for j in range(k,-1,-1):
                if j==2:
                    a=dp[i+1][j-1] - prices[i]
                    b=dp[i+1][j]
                    dp[i][j]=max(a,b)
                elif j==1:
                    d=dp[i+1][j+1] + prices[i]
                    e=dp[i+1][j]
                    dp[i][j]=max(d,e)
        return dp[0][k]
        