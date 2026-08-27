class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n=len(nums)
        res=[0] *n
        for i in range(n):
            res[i]=1
            for j in range(0,i):
                if nums[i]> nums[j]:
                    res[i]=max(res[i],res[j]+1)
        p=max(res)
        return p
                