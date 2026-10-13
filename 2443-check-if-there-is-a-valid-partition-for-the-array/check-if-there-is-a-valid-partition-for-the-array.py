class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        dp = {}

        def valid(left):
            if len(left) < 2 or len(left) > 3:
                return False

            take = len(left) == 2 and left[0] == left[1]

            if len(left) == 3:
                if left[0] == left[1] == left[2]:
                    take = True
                elif left[0] + 1 == left[1] and left[1] + 1 == left[2]:
                    take = True

            return take

        def check(i):
            if i == len(nums):
                return True

            if i in dp:
                return dp[i]

            for j in range(i, min(i + 3, len(nums))):
                left = nums[i:j + 1]

                if valid(left):
                    if check(j + 1):
                        dp[i] = True
                        return True

            dp[i] = False
            return False

        return check(0)