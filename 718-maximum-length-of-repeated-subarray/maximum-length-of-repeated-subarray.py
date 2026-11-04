class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        dp = [[[0] * 2 for _ in range(m+1)] for _ in range(n+1)]

        ans = 0

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):

                # find == True
                if nums1[i] == nums2[j]:
                    dp[i][j][1] = 1 + dp[i+1][j+1][1]

                # find == False
                take = 0
                skip = 0

                if nums1[i] == nums2[j]:
                    take = 1 + dp[i+1][j+1][1]

                skip = max(dp[i][j+1][0], dp[i+1][j][0])

                dp[i][j][0] = max(take, skip)

                ans = max(ans, dp[i][j][0], dp[i][j][1])

        return ans