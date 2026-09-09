class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        res=float('inf')
        while low<=high:
            mid=(low+high)//2
            
            if nums[low]>nums[mid]:
                res=min(nums[mid],res)
                high=mid-1
            else:
                res=min(nums[low],res)
                low=mid+1    
        return res

