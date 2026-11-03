class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in dp:
                return [dp[rem], i]

            dp[nums[i]] = i