class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1] * 3 for _ in range(n)]
        def best(i,k):
            if i==n:
                return 0
            if dp[i][k] != -1:
                return dp[i][k]
            if k==2:
                c=best(i+1,k-1) -prices[i]
                c1=best(i+1,k)
                dp[i][k]=max(c,c1)
                return dp[i][k]
            elif k==1:
                c=best(i+1,k+1) + prices[i]
                c1=best(i+1,k)
                dp[i][k]=max(c,c1)
                return dp[i][k]
        return best(0,2)