class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        if len(nums)==1:
            return nums[0]
        while low<=high:
            mid=(low+high)//2
            if mid<len(nums)-1 and (nums[mid] != nums[mid+1]) and (nums[mid] != nums[mid-1]):
                return nums[mid]    
            if mid<len(nums)-1 and mid%2==1 and nums[mid]==nums[mid+1]:
                high=mid-1
            elif mid%2==1 and nums[mid]==nums[mid-1]:
                low=mid+1
            elif mid<len(nums)-1 and mid%2==0 and nums[mid]==nums[mid+1]:
                low=mid+1
            elif mid<len(nums)-1 and  mid%2==0 and nums[mid]==nums[mid-1]:
                high=mid-1
            elif mid==len(nums)-1 and nums[mid]!=nums[mid-1]:
                return nums[mid]
            elif mid==0 and nums[mid]!=nums[mid+1]:
                return nums[mid]
            
        return 0