class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low=0
        count=0
        zero=0
        res=float(-inf)
        for high in range(len(nums)):
            if nums[high]==0:
                zero+=1
            while zero>k:
                if nums[low]==0:
                    zero-=1
                low+=1
            count=high-low+1
            res=max(res,count)
        return res
