class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        p=-99
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                p=i
                break
        if p==-99:
            return nums.reverse()
        for i in range(len(nums)-1,p,-1):
            if nums[i] > nums[p]:
                nums[p],nums[i]=nums[i],nums[p]
                break
        
        z=nums[p+1:]
        z.reverse()
        nums[p + 1:] = z
        
        

        
                
        

                