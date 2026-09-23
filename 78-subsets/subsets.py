class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        temp=[]
        def sub(i):
            nonlocal ans
            nonlocal temp
            if i==len(nums):
                ans.append(temp.copy())
                return
            temp.append(nums[i])
            sub(i+1)
            temp.pop()
            sub(i+1)
        sub(0)
        return ans