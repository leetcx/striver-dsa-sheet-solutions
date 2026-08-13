class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        ans=[]
        n=len(nums)
        def back(i):
            if i==n:
                if len(temp) == len(set(temp)):
                    ans.append(temp.copy())
                return 
            for j in range(n):
                temp.append(nums[j])
                back(i+1)
                temp.pop()
        back(0)
        return ans