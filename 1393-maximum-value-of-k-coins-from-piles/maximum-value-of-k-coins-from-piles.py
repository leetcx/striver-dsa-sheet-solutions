class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        dp={}
        def maxii(i,k):
            if i>=len(piles):
                return 0
            if k==0:
                return 0
            state=(i,k)
            if state in dp:
                return dp[state]
            nottaken=maxii(i+1,k)
            sum1=0
            taken=0
            for j in range(min(k,len(piles[i]))):
                sum1+=piles[i][j]
                taken=max(taken,sum1+ maxii(i+1,k-(j+1)))
            dp[state]= max(taken,nottaken)
            return dp[state]
        return maxii(0,k)
            
