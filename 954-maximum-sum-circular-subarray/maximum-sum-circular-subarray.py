class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum=nums[0]
        minsum=nums[0]
        res=nums[0]
        t=sum(nums)
        minres=float('inf')
        for i in range(1,len(nums)):
            maxsum=max(nums[i],maxsum+nums[i])
            minsum=min(nums[i],nums[i]+minsum)
            minres = min(minres, minsum)

            
            res=max(res,maxsum)
        if res<0:
            return res
        circu=t-minres
        return max(res,circu)