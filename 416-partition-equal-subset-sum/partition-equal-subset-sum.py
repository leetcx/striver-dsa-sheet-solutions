class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        p=sum(nums)
        d=p%2
        if d != 0:
            return False
        z=p//2
        n=len(nums)
        dp=[[None] * (z+1) for _ in range(n+1)]
        def check(sum1,i):
            if i >=len(nums):
                return False
            if sum1==0 and (len(nums)-i)>0:
                return True
            if dp[i][sum1] != None:
                return dp[i][sum1]
            take=False
            if nums[i] <= sum1:
                take = check(sum1-nums[i],i+1)
            skip=check(sum1,i+1)
            dp[i][sum1]=take or skip
            return dp[i][sum1]
        return check(z,0)
