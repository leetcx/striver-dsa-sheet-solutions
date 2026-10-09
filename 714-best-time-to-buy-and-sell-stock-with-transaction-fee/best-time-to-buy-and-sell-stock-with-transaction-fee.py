class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        dp={}
        def calculate(i,canbuy):
            if i >=len(prices):
                return 0
            state=(i,canbuy)
            if state in dp:
                return dp[state]
            profit=float('-inf')
            if canbuy==True:
                profit=-prices[i]+calculate(i+1,False)
                skip=calculate(i+1,True)
                
            else:
                profit=(prices[i]-fee)+calculate(i+1,True)
                skip=calculate(i+1,False)
            dp[state]= max(profit,skip)
            return dp[state]
        return calculate(0,True)
            