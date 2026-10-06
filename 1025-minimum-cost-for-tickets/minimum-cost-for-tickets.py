class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp = [0] * (days[-1]+1)
        m=len(days)
        travel=set()
        for i in days:
            travel.add(i)
        for i in range(1,(days[-1]+1)):
            
            if i not in travel:
                dp[i]=dp[i-1]
                continue
            

               
                
            buy1 = costs[0] + dp[max(0,i-1)]
            buy2 = costs[1] + dp[max(0,i - 7)]
            buy3 = costs[2] + dp[max(0,i - 30)]
                
            dp[i] = min(buy1, buy2, buy3)
        return dp[days[-1]]

       