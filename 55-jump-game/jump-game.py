class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums)==1:
            return True
        dp=[0] * (len(nums))
        dp[0]=1
        for i in range(len(nums)):
            if dp[i]==0:
                return False
            for j in range(i+1,min(len(nums),nums[i]+i+1)) :
                dp[j]=1
        return dp[-1]==1  