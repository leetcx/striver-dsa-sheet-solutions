class Solution:
    def lenLongestFibSubseq(self, nums: list[int]) -> int:
        n = len(nums)
        mp = {num: i for i, num in enumerate(nums)}
        dp = {}

        def mini(i, j):
            state = (i, j)
            if state in dp:
                return dp[state]

            p = nums[i] + nums[j]

            if p in mp:
                k = mp[p]
                dp[state] = 1 + mini(j, k)
                return dp[state]

            return 0

        ans = 0

        for i in range(n):
            for j in range(i+1, n):
                score = 2 + mini(i, j)
                ans = max(ans, score)

        return ans if ans >= 3 else 0

            