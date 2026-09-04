class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestend=nums[0]

        res=nums[0]
        for i in range(1,len(nums)):
            bestend=max(nums[i],bestend+nums[i])
            res=max(res,bestend)
        return res