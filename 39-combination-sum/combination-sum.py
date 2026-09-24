class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans=[]
        temp=[]
        def combine(i,sum1):
            if sum1>target:
                return
            if sum1==target:
                ans.append(temp.copy())
                return
            if i >=len(nums):
                return
            temp.append(nums[i])
            combine(i,sum1+nums[i])
            temp.pop()
            
            combine(i+1,sum1)
            
        combine(0,0)
        return ans