class Solution:
    def findLongestChain(self, nums: list[list[int]]) -> int:
        nums.sort()
        z=len(nums)
        count=0
        maxlength=float('-inf')
        ans=1
        dp=[[-1] * (z+1) for _ in range(z+1)]
        used=[False] * len(nums)
        def calculate(i,prev):
            nonlocal count
            nonlocal maxlength
            nonlocal ans
            if i>=len(nums):
                return 0
            if prev != -1:

                if dp[i][prev] != -1:
                    return dp[i][prev]
            take=0
            if i>=0 and i <len(nums) :
                
                if (prev==-1 or nums[prev][1] < nums[i][0]) :
                    take = 1+ calculate(0,i)   
                    skip= calculate(i+1,prev)
                else:
                    skip=calculate(i+1,prev)
            if prev != -1:
                dp[i][prev]=max(take,skip)
            return max(take,skip)
        return calculate(0,-1)
        

