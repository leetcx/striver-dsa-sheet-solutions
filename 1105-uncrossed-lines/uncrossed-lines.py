class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        dp={}
        def uncrossed(i,j):
            if i>=len(nums1) or j>= len(nums2):
                return 0
            state=(i,j)
            if state in dp:
                return dp[state]
            take=float('-inf')
            if nums1[i]==nums2[j]:
                take=1+uncrossed(i+1,j+1)
            skip1=uncrossed(i+1,j)
            skip2=uncrossed(i,j+1)
            dp[state]= max(take,skip1,skip2)
            return dp[state]
        return uncrossed(0,0)
