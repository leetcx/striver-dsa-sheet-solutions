class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        first=[]
        dp={}
        def maxi(i,p):
            if p==0:
                return 0,first.copy()
            if len(nums) - i < p*k:
                return float('-inf'), first.copy()
            state=(i,p)
            if state in dp:
                return dp[state]
            skip,skip_indices=maxi(i+1,p)
            first.append(i)
            val,indices= maxi(i+k,p-1)
            take=sum(nums[i:i+k])+val
            first.pop()
            if take > skip or (take == skip and [i] + indices < skip_indices):
                dp[state]= take, [i] + indices
                return dp[state]
            dp[state]= skip, skip_indices
            return dp[state]
        maxuu,ans=maxi(0,3)
        return ans[:3]
                  