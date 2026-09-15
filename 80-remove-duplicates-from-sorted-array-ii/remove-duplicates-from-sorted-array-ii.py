class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c=1
        p=1
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                c+=1
            else:
                c=1
            if c<3 :
                nums[p]=nums[i]
                p+=1
            
        return p


