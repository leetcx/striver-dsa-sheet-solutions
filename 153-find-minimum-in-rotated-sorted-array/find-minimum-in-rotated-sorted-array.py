class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        h=n-1
        l=0
        while l<h:
            mid=(l+h)//2
            if nums[mid]>=nums[h]:
                l=mid+1
            else:
                h=mid
        return nums[h]
            
