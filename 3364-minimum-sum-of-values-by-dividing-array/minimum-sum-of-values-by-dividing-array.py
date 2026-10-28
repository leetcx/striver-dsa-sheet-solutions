from typing import List

class Solution:
    def minimumValueSum(self, nums: List[int], andvalues: List[int]) -> int:
        n = len(nums)
        m = len(andvalues)
        dp = {}
        def lesgo(i, j,andop):
            if j == m:
                return 0 if i == n else float('inf')

            if i >= n:
                return float('inf')
            state=(i,j,andop)
            if state in dp:
                return dp[state]
            including=float('inf')
            if (andop & nums[i]) == andvalues[j]:
                including=nums[i]+lesgo(i+1,j+1,(1<<17)-1)
            excluding=lesgo(i+1,j,andop & nums[i])
            dp[state]= min(including,excluding)
            return dp[state]
        ans=lesgo(0,0,(1<<17)-1)
        if ans==float('inf'):
            return -1
        return ans

            