class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        p=sorted(nums)
        low=0
        high=len(nums)-1
        found=False
        done=False
        point=0
        second=0
        for i in range(len(nums)):
            if not found and p[low]!=nums[low]:
                point=low
                found=True
            else:
                low+=1
            if not done and p[high]!=nums[high]:
                second=high
                done=True
            else:
                high-=1
        if point ==0 and second==0:
            return 0
        subarr=nums[point:second+1]
        g=len(subarr)
        return g


