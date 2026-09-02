class Solution:
    def maxArea(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        res=float('-inf')
        while low<high:
            if nums[low]<nums[high]:
                p=nums[low]*(high-low)
                res=max(res,p)
                low+=1
            elif nums[high]<=nums[low]:
                p=nums[high]*(high-low)
                res=max(res,p)
                high-=1
        return res

          