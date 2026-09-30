class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)

        keys = sorted(set(nums[i] - i for i in range(n)))

        rank = {key: i + 1 for i, key in enumerate(keys)}

        bit = [float('-inf')] * (len(keys) + 1)

        def update(i, value):
            while i <= len(keys):
                bit[i] = max(bit[i], value)
                i += i & -i

        def query(i):
            ans = float('-inf')
            while i > 0:
                ans = max(ans, bit[i])
                i -= i & -i
            return ans

        ans = float('-inf')

        for i in range(n):
            key = nums[i] - i
            idx = rank[key]

            best = query(idx)

            dp = nums[i]

            if best != float('-inf'):
                dp = max(dp, nums[i] + best)

            update(idx, dp)

            ans = max(ans, dp)

        return ans