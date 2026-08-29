class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n= len(nums)
        res=[0] * (n+1)
        res[0]=1
        for i in range(1,n):
            res[i]=1
            for j in range(0,i):
                if nums[j] < nums[i] :
                    res[i]= max(res[i],res[j]+1)
        p=max(res)
        return p

                 
       