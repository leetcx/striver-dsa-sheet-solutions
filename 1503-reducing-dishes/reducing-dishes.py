class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [[0] * 502 for _ in range(501)]
        for i in range(n-1,-1,-1):
            for j in range(n,0,-1):
                
            
            
                
                take=(satisfaction[i]*j)+dp[i+1][j+1]
                
                skip=dp[i+1][j]
                dp[i][j]= max(take,skip)
            
        return dp[0][1]

            