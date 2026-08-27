class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1] * 3 for _ in range(n)]
        def best(i,trans):
           
            if i==n or trans==0:
                return 0
            if dp[i][trans] != -1:
                return dp[i][trans]
            elif trans==1:
                c=best(i+1,trans-1) + prices[i]
                c1=best(i+1,trans)
                
            else:
                
                c=best(i+1,trans-1) - prices[i]
                c1=best(i+1,trans)
            dp[i][trans] =max(c,c1)
            return dp[i][trans]
        return best(0,2)

            