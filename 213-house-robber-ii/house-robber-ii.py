class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums) 

        memo = [0] * (n + 1)

        # Case 1: take nums[0], so we cannot take nums[n-1]
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(2, n):
            if i-1>=0:
                
                take = nums[i - 1] + memo[i - 2]
            skip = memo[i - 1]
            memo[i] = max(take, skip)

        result1 = memo[n - 1]

        # Case 2: skip nums[0], so nums[1] can be considered
        memo = [0] * (n + 1)
        memo[0] = 0
        memo[1] = 0

        for i in range(2, n + 1):
            if i-1>=0:
                
                take = nums[i - 1] + memo[i - 2]
            skip = memo[i - 1]
            memo[i] = max(take, skip)

        result2 = memo[n]
        if len(nums)==1:
            return nums[0]

        return max(result1, result2)