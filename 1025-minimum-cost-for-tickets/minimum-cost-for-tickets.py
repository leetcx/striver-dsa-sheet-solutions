class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp={}
        def mincost(i,available):
            if i>=len(days):
                return 0
            state=(i,available)
            if state in dp:
                return dp[state]
            buy1=float('inf')
            buy2=float('inf')
            buy3=float('inf')
            skip1=float('inf')
            if days[i]>=available:
                
                buy1=costs[0]+mincost(i+1,days[i]+1)
                buy2=costs[1]+mincost(i+1,days[i]+7)
                buy3=costs[2]+mincost(i+1,days[i]+30)
            else:
                skip1=mincost(i+1,available)
            dp[state]= min(buy1,buy2,buy3,skip1)
            return dp[state]
        return mincost(0,0)