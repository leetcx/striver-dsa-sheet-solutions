class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[-1]:
                if target>nums[-1] and nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if target<=nums[-1] and nums[mid]>target:
                    high=mid-1
                else:
                    if target>nums[-1]:
                        high=mid-1
                    else:
                        low=mid+1  
                
        return -1

