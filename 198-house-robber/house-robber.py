class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1] * 2 for _ in range(n+1)]
        for i in range(2):
            dp[n][i]=0
        for i in range(n+1):
            dp[i][0]=0
        for i in range(n-1,-1,-1):
            for j in range(1,-1,-1):
                if j==1:
                    c=nums[i]+ dp[i+1][j-1]
                    p=dp[i+1][j]
                    dp[i][j]=max(p,c)

                else:
                    dp[i][j]=dp[i+1][j+1]
        return dp[0][1]