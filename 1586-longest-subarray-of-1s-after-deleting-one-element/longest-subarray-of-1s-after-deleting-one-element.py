class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        low=0
        zero=0
        res=float('-inf')
        for high in range(len(nums)):
            if nums[high]==0:
                zero+=1
            while zero>1:
                if nums[low]==0:
                    zero-=1
                low+=1
            l=high-low
            res=max(res,l)
        return res
            
