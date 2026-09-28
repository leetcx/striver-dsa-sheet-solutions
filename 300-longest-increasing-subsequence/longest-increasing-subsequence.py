class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def increasing(i):
            if memo[i] != -1:
                return memo[i]

            ans = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    ans = max(ans, 1 + increasing(j))

            memo[i] = ans
            return memo[i]

        ans = 1

        for i in range(n):
            ans = max(ans, increasing(i))

        return ans
        


