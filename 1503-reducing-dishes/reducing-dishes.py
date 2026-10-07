class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        dp={}
        def maxprofit(i,j):
            if i>=len(satisfaction):
                return 0
            state=(i,j)
            if state in dp:
                return dp[state]
            
            
                
            take=(satisfaction[i]*j)+maxprofit(i+1,j+1)
                
            skip=maxprofit(i+1,j)
            dp[state]= max(take,skip)
            return dp[state]
        return maxprofit(0,1)

            