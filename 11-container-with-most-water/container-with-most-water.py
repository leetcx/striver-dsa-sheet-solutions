class Solution:
    def maxArea(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        res=float('-inf')
        while low<high:
            if nums[low]<nums[high]:
                area=nums[low] * (high-low)
                res=max(res,area)
                low+=1
            elif nums[low]>nums[high]:
                area=nums[high] * (high-low)
                res=max(res,area)
                high-=1
            else:
                area=nums[high] * (high-low)
                res=max(res,area)
                low+=1
                
        return res
            