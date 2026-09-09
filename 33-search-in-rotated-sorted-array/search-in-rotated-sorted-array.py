class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        p=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>nums[p-1]:
                if nums[mid]==target:
                    return mid
                if nums[mid]<target:
                    low=mid+1
                else:
                    if target>=nums[0]:
                        high=mid-1
                    else:
                        low=mid+1
            else:
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    high=mid-1
                else:
                    if target>nums[p-1]:
                        high=mid-1
                    else:
                        low=mid+1
        return -1
