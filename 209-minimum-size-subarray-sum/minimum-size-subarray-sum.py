class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        high=0
        res=float('inf')
        sum1=0
        for high in range(len(nums)):
            sum1+=nums[high]
            while sum1>=target:
                res=min(res,high-low+1)
                sum1-=nums[low]
                low+=1
            
        if res==float('inf'):
            return 0
        return res