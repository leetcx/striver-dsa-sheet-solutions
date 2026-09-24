class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        
        dp=[-1] * 1000
        def combo(i,sum1):
            count=0
            if sum1>target:
                return 0
            if sum1==target:
                return 1
                
            if i>=len(nums):
                return 0
            if dp[sum1] != -1:
                return dp[sum1]
            count+=combo(0,sum1+nums[i])
            count+=combo(i+1,sum1)
            dp[sum1]=count
            return count
        return combo(0,0)

