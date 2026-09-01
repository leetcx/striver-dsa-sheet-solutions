class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        low=0
        high=0
        sum1=sum(nums)
        t=sum1-x
        res=float('-inf')
        sui=0
        
        for high in range(len(nums)):

            sui+=nums[high]
            hei=high-low+1
            while sui>t and low<=high:
                sui-=nums[low]
                low+=1
                hei=high-low+1

            if sui==t:
                res=max(res,high-low+1)
        if res==float('-inf'):
            return -1
        g=len(nums) - res
        return g
