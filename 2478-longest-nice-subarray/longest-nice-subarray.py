class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        low=0
        high=0
        res=float('-inf')
        current=0

        for high in range(len(nums)):
            
            
            while current & nums[high] !=0:
                current = current ^ nums[low]
                low+=1
                lou=high-low+1
            current=current | nums[high]
            lou=high-low+1
            res=max(res,lou)
        if res==float('-inf'):
            return 1
        return res
