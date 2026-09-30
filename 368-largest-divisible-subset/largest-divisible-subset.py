class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        n = len(nums)

        dp = [[None] * (n + 1) for _ in range(n)]

        def cal(i, prev):

            if i >= n:
                return []

            if dp[i][prev] is not None:
                return dp[i][prev]

            take = []

            if prev == -1 or nums[i] % nums[prev] == 0:
                take = [i] + cal(i + 1, i)

            skip = cal(i + 1, prev)

            if len(take) > len(skip):
                dp[i][prev] = take
            else:
                dp[i][prev] = skip

            return dp[i][prev]

        indices = cal(0, -1)

        return [nums[i] for i in indices]