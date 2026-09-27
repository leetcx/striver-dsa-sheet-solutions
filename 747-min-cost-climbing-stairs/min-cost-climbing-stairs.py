class Solution:
    def minCostClimbingStairs(self, nums: list[int]) -> int:
        memo=[-9999] * len(nums)
        ans=float('inf')
        def mincost(i):
            if i>=len(nums):
                return 0
            if memo[i] != -9999:
                return memo[i]
            take1=nums[i]+mincost(i+1)
            take2=nums[i]+mincost(i+2)
            memo[i]=min(take1,take2)
            return memo[i]
        for i in range(0,2):
            ans=min(ans,mincost(i))
        return ans