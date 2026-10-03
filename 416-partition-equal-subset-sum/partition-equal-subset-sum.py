class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        p=sum(nums)
        d=p%2
        if d != 0:
            return False
        z=p//2
        n=len(nums)
        dp=[[None] * (z+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(z+1):
                if i==0:
                    dp[i][j]=False 
                    continue   
                if j==0 and i>0:
                    dp[i][j]= True
                    continue
                
                take=False
                if nums[i-1] <= j:
                    take = dp[i-1][j-nums[i-1]]
                skip=dp[i-1][j]
                dp[i][j]=take or skip
           
        return dp[n][z]
