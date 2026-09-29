class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]
        def take1(i,prev):
            if i>= len(nums):
                return 0
            if prev!= -1 and memo[i][prev] != -1:
                return memo[i][prev]
            take=0
            if prev==-1 or  nums[prev] < nums[i]:
                take=1+take1(i+1,i)
                skip=take1(i+1,prev)
            else:
                skip=take1(i+1,prev)
            memo[i][prev]= max(take,skip)
            return memo[i][prev]
        return take1(0,-1)
