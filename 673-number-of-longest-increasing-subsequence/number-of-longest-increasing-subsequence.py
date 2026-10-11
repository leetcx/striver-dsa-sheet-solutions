class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        dp = {i: [1, 1] for i in range(len(nums))}
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    z=dp[j][0]+1
                    if z>dp[i][0]:
                        dp[i][0]=z
                        dp[i][1]=dp[j][1]
                    elif z==dp[i][0]:
                        dp[i][1]+=dp[j][1]
        longest = max(dp[i][0] for i in range(len(nums)))
        ans=0
        for i in range(len(nums)):
            if dp[i][0]==longest:
                ans+=dp[i][1]
        return ans

