class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        p=len(nums)
        while low<=high:
            mid=(low+high)//2
            if mid !=0 and mid !=p-1 and nums[mid] < nums[mid-1]  and nums[mid] < nums[mid+1]:
                return nums[mid]
            if nums[mid] > nums[p-1]:
                low=mid+1
            else:
                high=mid-1
        return min(nums)