class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        maxpro=float('-inf')
        low=0
        high=0
        while low<=high and high<len(nums):
            if nums[low]>=nums[high]:
                low=high
                high+=1
                
            else:
                
                profit=nums[high]-nums[low]
                maxpro=max(maxpro,profit)
                high+=1
        if maxpro==float('-inf'):
            return 0
        return maxpro

