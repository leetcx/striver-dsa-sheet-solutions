class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        lastinval=-1
        lastval=-1
        res=0
        for high in range(len(nums)):
            if nums[high] > right:
                lastinval=high
            if left<=nums[high]<=right:
                lastval=high
            res+=max(0,lastval-lastinval)
        return res


            