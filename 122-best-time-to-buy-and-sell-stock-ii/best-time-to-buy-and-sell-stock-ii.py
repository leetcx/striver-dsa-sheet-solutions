class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        low=0
        high=0
        sum1=0
        while low<=high and high<len(nums):
            if nums[low] >= nums[high]:
                low=high
                high+=1
            else:
                sum1+=nums[high]-nums[low]
                low+=1
                high+=1
        return sum1