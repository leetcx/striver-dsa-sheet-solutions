class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        ans=0
        sum1=0
        memo = [[None] * 2 for _ in range(len(nums))]
        choosen=False
        def maxii(i,choosen):
            if i>=len(nums):
               
                return 0
            if memo[i][choosen] != None:
                return memo[i][choosen]
            
            if choosen==False:
                take=nums[i] + maxii(i+1,True)
                skip=maxii(i+1,choosen)
            else:
                take=-nums[i] + maxii(i+1,False)
                skip=maxii(i+1,choosen)
            memo[i][choosen]=max(take,skip)
            return memo[i][choosen]
        return maxii(0,False)