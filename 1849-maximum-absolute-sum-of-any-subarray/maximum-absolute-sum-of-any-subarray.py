class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        best=nums[0]
        ans=abs(nums[0])
        worst=nums[0]
        for i in range(1,len(nums)):
            v1=best+nums[i]
            v2=(nums[i])
            v3=worst+nums[i]
            worst=min(v2,v3)
            best=max(v1,v2)
            ans=max(ans,abs(best),abs(worst))
        return ans