class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp={}
        def count(i,sum1):
            take=0
            if i==len(nums) and sum1==target:
                return 1
            if i>=len(nums):
                return 0
            if (i,sum1) in dp:
                return dp[(i,sum1)]
            take+=count(i+1,sum1+nums[i])
            take+=count(i+1,sum1+(-nums[i]))
            dp[(i,sum1)]=take
            return take

        return count(0,0)


            
            