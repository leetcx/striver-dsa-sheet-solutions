class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans=[]
        temp=[]
        def combine(p,sum1):
            if sum1>target:
                return
            if sum1==target:
                ans.append(temp.copy())
                return
            for i in range(p,len(nums)):
                temp.append(nums[i])
                combine(i,sum1+nums[i])
                temp.pop()
                
        combine(0,0)
        return ans