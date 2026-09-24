class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        temp=[]
        def organ(i):
            nonlocal temp
            nonlocal ans
            if i==len(nums):
                ans.append(temp.copy())
                return
            temp.append(nums[i])
            organ(i+1)
            temp.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            organ(i+1)
               
            
        organ(0)
        return ans
            
                
        

