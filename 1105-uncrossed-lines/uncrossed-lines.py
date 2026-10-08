class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        p=len(nums1)
        t=len(nums2)
        dp=[[0] * (t+1) for _ in range(p+1)]
        for i in range(p-1,-1,-1):
            for j in range(t-1,-1,-1):
           
                take=float('-inf')
                if nums1[i]==nums2[j]:
                    take=1+dp[i+1][j+1]
                skip1=dp[i+1][j]
                skip2=dp[i][j+1]
                dp[i][j]= max(take,skip1,skip2)
            
        return dp[0][0]
