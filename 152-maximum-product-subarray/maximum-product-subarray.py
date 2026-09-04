class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best=nums[0]
        ans=nums[0]
        worst=nums[0]
        for i in range(1,len(nums)):
            v1=best * nums[i]
            v2=worst * nums[i]
            v3=nums[i]
            best=max(v3,max(v1,v2))
            worst=min(v3,min(v1,v2))
            ans=max(ans,max(best,worst))
        return ans