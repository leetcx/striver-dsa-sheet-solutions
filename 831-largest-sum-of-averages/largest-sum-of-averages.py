class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        dp={}
        def lesgo(i,k):
            if i>=len(nums):
                if k==0:
                    return 0
                return float('-inf')
            
            state=(i,k)
            if state in dp:
                return dp[state]
            maxscore=float('-inf')
            for j in range(i,len(nums)):
                score=sum(nums[i:j+1])/len(nums[i:j+1]) + lesgo(j+1,k-1)
                maxscore=max(score,maxscore)
            dp[state]= maxscore
            return dp[state]
        return lesgo(0,k)