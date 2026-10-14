class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        dp={}
        def subseq(i,j):

            if i >= len(nums1) or j >= len(nums2):
                
                
                return float('-inf')
            state=(i,j)
            if state in dp:
                return dp[state]

          
            take = nums1[i] * nums2[j] + max(0, subseq(i+1, j+1))
            skip1=subseq(i+1,j)
            skip2=subseq(i,j+1)
            dp[state]= max(take,skip1,skip2)
            return dp[state]
        return subseq(0,0)
        