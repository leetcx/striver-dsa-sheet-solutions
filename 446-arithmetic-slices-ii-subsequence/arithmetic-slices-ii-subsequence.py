class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n=len(nums)
        dp = [dict() for _ in range(n)]
        prev=0  
        ans=0 
        for i in range(len(nums)) :
            for j in range(i):
                diff=nums[i]-nums[j]
                if diff in dp[j] :
                    prev=dp[j][diff]
                else:
                    prev=0
                if diff in dp[i]:
                    dp[i][diff]+=prev+1
                else:
                    dp[i][diff]=prev+1
                ans+=prev
        return ans
                