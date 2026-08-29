class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
       
        low=1
        high=len(nums)-2
        found=False
        done=False
        point=0
        second=0
        for i in range(len(nums)):
            if low<len(nums) and nums[low]< nums[low-1]:
                point=low-1
                break
            else:
                low+=1
        for i in range(len(nums)-2,-1,-1):
            if high>=0 and nums[high] > nums[high+1]:
                second=high+1
                break
            else:
                high-=1
        if second==0 and point==0:
            return 0
        mini=min(nums[point:second+1])
        maxi=max(nums[point:second+1])
        while point>0 and mini<nums[point-1]:
            point-=1
        while second<len(nums)-1 and maxi>nums[second+1]:
            second+=1
        p=(second+1)-point
        return p
        
               
            