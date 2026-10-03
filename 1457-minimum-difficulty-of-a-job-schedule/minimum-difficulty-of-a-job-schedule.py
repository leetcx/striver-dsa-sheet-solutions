class Solution:
    def minDifficulty(self, nums: list[int], d: int) -> int:
        p = len(nums)

        if d > p:
            return -1

        dp = [[-1] * (d + 1) for _ in range(p + 1)]

        def choose(d, idx):
            if d == 1:
                return max(nums[idx:])

            if dp[idx][d] != -1:
                return dp[idx][d]

            maxd = float('-inf')
            finalresult = float('inf')

            for i in range(idx, len(nums) - d + 1):
                maxd = max(maxd, nums[i])

                result = maxd + choose(d - 1, i + 1)

                finalresult = min(finalresult, result)

            dp[idx][d] = finalresult
            return dp[idx][d]

        return choose(d, 0)
