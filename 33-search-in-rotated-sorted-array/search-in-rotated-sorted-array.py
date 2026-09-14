class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        d=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[d-1]:
                if nums[mid]>target and target> nums[-1]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target and target<=nums[-1] :
                    low=mid+1
                else:
                    high=mid-1
        return -1