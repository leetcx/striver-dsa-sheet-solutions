class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[-1] * (len(nums)+1)
        for i in range(len(nums)+1):
            if i==0:
                dp[i]=0
                continue
            if i==1:
                dp[i]=nums[0] 
                continue   

            
            take=nums[i-1]+ dp[i-2]
            skip=dp[i-1]
            dp[i]= max(take,skip)
            
        return dp[len(nums)]