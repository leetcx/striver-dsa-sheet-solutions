class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        high=0
        sum1=0
        res=float('inf')
        for high in range(0,len(nums)):
            sum1+=nums[high]
            while sum1>=target and low<=high:
                l=high-low+1
                res=min(l,res)
                sum1-=nums[low]
                low+=1
        if res==float('inf'):
            return 0
        return res
                

