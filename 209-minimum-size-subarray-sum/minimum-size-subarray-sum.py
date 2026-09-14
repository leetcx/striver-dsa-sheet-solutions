class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum1=0
        low=0
        res=0
        d=float('inf')
        p=len(nums)
        for high in range(0,len(nums)):
            sum1+=nums[high]
            while sum1>=target and low<=high:
                res=high-low+1
                if d>res:
                    d=res
                sum1-=nums[low]
                low+=1
        if d==float('inf'):
            return 0
        return d
        
            

