class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        low=0
        count=0
        p=1
        for high in range(len(nums)):
            p=p*nums[high]
            while p>=k and low<=high:
                p=p//nums[low]
                low+=1
            count+=high-low+1
        return count
