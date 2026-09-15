class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sum1=0
        low=0
        res=float('inf')
        for high in range(len(nums)):
            sum1+=nums[high]
            while sum1>=target:
                res=min(res,high-low+1)
                sum1-=nums[low]
                low+=1
        if res==float('inf'):
            return 0
        return res