class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        low=0
        high=0
        p=1
        count=0
        for high in range(0,len(nums)):
            p=p*nums[high]
            while p>= k and low<high:
               
                p=p//nums[low]
                low+=1
            if p<k:
                count+=high-low+1
        return count

            