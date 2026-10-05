class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp=[[-99] * (len(prices)+1) for _ in range(len(prices)+1) ]
        def maxprofit(i,prev):
            if i >=len(prices):
                return 0
            
            if dp[i][prev] != -99:
                return dp[i][prev]
            
            buy=float('-inf')
            notbuy=float('-inf')
            sell=float('-inf')
            notsell=float('-inf')
            if prev==-1 :
                buy=maxprofit(i+1,i)-prices[i]
                notbuy=maxprofit(i+1,prev)
            else:
                sell=prices[i]+maxprofit(i+2,-1)
                notsell=maxprofit(i+1,prev)
            dp[i][prev]= max(buy,notbuy,sell,notsell)
            return dp[i][prev]
        return maxprofit(0,-1)