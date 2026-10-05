class Solution:
    def rob(self, nums: list[int]) -> int:
        a=nums[0]
        b=0
        for i in range(1,len(nums)):
            take=nums[i]+b
            skip=a
            curr=max(take,skip)

            
            b=a
            a=curr    
            
        return a