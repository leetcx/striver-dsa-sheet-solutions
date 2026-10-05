class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[-1] * (len(nums)+1)
        def profit(i):
            if i>=len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            take=nums[i]+profit(i+2)
            skip=profit(i+1)
            dp[i]= max(take,skip)
            return dp[i]
        return profit(0)