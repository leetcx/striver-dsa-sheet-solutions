class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp=[]
        ans=[]
       
        def backtrack(i):
            
            ans.append(temp.copy())
               
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                

                temp.append(nums[j])
                backtrack(j + 1)
                temp.pop()

        backtrack(0)
        return ans
                
               
                    
                
                  