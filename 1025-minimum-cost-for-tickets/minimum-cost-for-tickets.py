class Solution:
    def mincostTickets(self, days: list[int], cost: list[int]) -> int:
        days.sort()
        dp={}
        def ways(i):
            if i>days[-1]:
                return 0
            if i in dp:
                return dp[i]
            skip=float('inf')
            if i in days:
                take1=cost[0]+ways(i+1)

                take2=cost[1]+ways(i+7)
                take3=cost[2]+ways(i+30)
            else:
                take1=cost[0]+ways(i+1)

                take2=cost[1]+ways(i+7)
                take3=cost[2]+ways(i+30)
                skip=ways(i+1)
            dp[i]= min(take1,take2,take3,skip)
            return dp[i]
        return ways(days[0])

