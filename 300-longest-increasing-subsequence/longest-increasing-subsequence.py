class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        prev=-1
        n=len(nums)
        dp=[[0] *(n+1) for _ in range(n+1)]
        for i in range(n):
            dp[n][i]=0
        for i in range(n-1,-1,-1):
            for j in range(i-1,-2,-1):
                if j==-1 or nums[j] < nums[i]:
                    dp[i][j+1]=max((1+dp[i+1][i+1]),(dp[i+1][j+1]))
                else:
                    dp[i][j+1]=dp[i+1][j+1]
        return dp[0][prev+1]
