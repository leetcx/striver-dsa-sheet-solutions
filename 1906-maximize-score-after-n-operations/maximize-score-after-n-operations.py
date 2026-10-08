class Solution:
    def maxScore(self, nums: list[int]) -> int:
        z = len(nums) // 2
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        dp={}
        def maxscore(l, i, j, nums):
            if l > z or i >= len(nums):
                return 0

            if j >= len(nums):
                return maxscore(l, i + 1, i + 2, nums)
            state=(l,i,j,tuple(nums))
            if state in dp:
                return dp[state]
            skip1 = maxscore(l, i + 1, i + 2, nums)
            skip2 = maxscore(l, i, j + 1, nums)

            subarr = []

            for p in range(len(nums)):
                if p != i and p != j:
                    subarr.append(nums[p])

            take = l * gcd(nums[i], nums[j]) + maxscore(
                l + 1, 0, 1, subarr
            )

            dp[state]= max(skip1, skip2, take)
            return dp[state]

        return maxscore(1, 0, 1, nums)