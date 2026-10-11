class Solution:
    def maxValue(self, nums: list[list[int]], k: int) -> int:
        nums.sort()
        n = len(nums)
        dp = {}

        def calculate(i, k):
            if i >= n or k == 0:
                return 0

            state = (i, k)
            if state in dp:
                return dp[state]

            low = i + 1
            high = n - 1
            j = n

            while low <= high:
                mid = (low + high) // 2

                if nums[mid][0] > nums[i][1]:
                    j = mid
                    high = mid - 1
                else:
                    low = mid + 1

            take = nums[i][2] + calculate(j, k - 1)
            skip = calculate(i + 1, k)

            dp[state] = max(take, skip)
            return dp[state]

        return calculate(0, k)