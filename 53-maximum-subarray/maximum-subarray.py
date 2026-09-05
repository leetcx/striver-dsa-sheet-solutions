class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            best=max(best+nums[i],nums[i])
            ans=max(ans,best)
        return ans