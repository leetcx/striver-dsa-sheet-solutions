class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(i):
                cd = nums[i] - nums[j]

                dp[i][cd] = dp[j].get(cd, 1) + 1
                ans = max(ans, dp[i][cd])

        return ans