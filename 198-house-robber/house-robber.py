class Solution:
    def rob(self, nums: list[int]) -> int:
        can=1
        money=0
        maxmoney=float("-inf")
        ans=0
        memo=[-9999] * len(nums)
        def mone(i):
            nonlocal can
            nonlocal money
            nonlocal maxmoney
            nonlocal ans
            if i>=len(nums):
                return 0
            if memo[i] != -9999:
                return memo[i]
                
            take=nums[i]+ mone(i+2)
            skip=mone(i+1)
            memo[i]=max(take,skip)
            return memo[i]
                
            
       
        return mone(0)
        

