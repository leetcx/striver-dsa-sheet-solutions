class Solution:
    def rob(self, nums: list[int]) -> int:

        def cal(start, end):
            memo = {}

            def solve(i):
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                take = nums[i] + solve(i + 2)
                skip = solve(i + 1)

                memo[i] = max(take, skip)

                return memo[i]

            return solve(start)

        if len(nums) == 1:
            return nums[0]

        return max(
            cal(0, len(nums) - 2),
            cal(1, len(nums) - 1)
        )