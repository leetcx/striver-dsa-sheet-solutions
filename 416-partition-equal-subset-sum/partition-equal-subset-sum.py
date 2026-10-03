class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        p=sum(nums)
        d=p%2
        if d != 0:
            return False
        z=p//2
        n=len(nums)
        dp=[[None] * (z+1) for _ in range(n+1)]
        def check(sum1,n):
            if n==0:
                return False
            if sum1==0 and n>0:
                return True
            if dp[n-1][sum1] != None:
                return dp[n-1][sum1]
            take=False
            if nums[n-1] <= sum1:
                take = check(sum1-nums[n-1],n-1)
            skip=check(sum1,n-1)
            dp[n-1][sum1]=take or skip
            return dp[n-1][sum1]
        return check(z,len(nums))
