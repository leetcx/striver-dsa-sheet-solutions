class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        used=[False] * len(nums)
        ans=[]
        temp=[]
        def all(i):
            nonlocal ans
            nonlocal temp
            nonlocal used
            if len(temp)==len(nums):
                ans.append(temp.copy())
                return
            if i >=len(nums):
                return
            if  used[i]==False:
                
                temp.append(nums[i])
                used[i]=True
                all(0)
                temp.pop()
                used[i]=False
            all(i+1)
        all(0)
        return ans