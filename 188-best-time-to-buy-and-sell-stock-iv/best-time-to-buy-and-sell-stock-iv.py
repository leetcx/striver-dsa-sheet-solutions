class Solution:
    def maxProfit(self, trans: int, prices: List[int]) -> int:
        n=len(prices)
        trans=trans*2
        dp=[[-1] * (trans+1) for _ in range(n)]
        def best(i,trans):
           
            if i==n or trans==0:
                return 0
            if dp[i][trans] != -1:
                return dp[i][trans]
            if trans%2==1:
                c=best(i+1,trans-1) + prices[i]
                c1=best(i+1,trans)
                
            elif trans %2==0 :
                
                c=best(i+1,trans-1) - prices[i]
                c1=best(i+1,trans)
            dp[i][trans] =max(c,c1)
            return dp[i][trans]
        return best(0,trans)

            