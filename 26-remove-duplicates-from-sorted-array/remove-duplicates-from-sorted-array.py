class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
        count=1
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                continue
           
            nums[count]=nums[i]
            count+=1
       
        return count