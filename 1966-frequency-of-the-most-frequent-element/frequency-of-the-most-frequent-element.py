class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        low=0
        high=0
        sum1=0
        res=float('-inf')
        for high in range(len(nums)):
            sum1+=nums[high]
            cost=nums[high] *(high-low+1)-sum1
            while cost>k:
                sum1-=nums[low]
                low+=1
                cost=nums[high] *(high-low+1)-sum1
            res=max(res,high-low+1)
        return res
            