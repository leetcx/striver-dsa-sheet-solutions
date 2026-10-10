class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        dp = [[0] * 1001 for _ in range(1500)]
        result = 1

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j] + 500

                if dp[j][diff] > 0:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2

                result = max(result, dp[i][diff])

        return result