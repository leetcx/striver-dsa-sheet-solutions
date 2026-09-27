class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        full = (1 << n) - 1

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(mask, last):
            if mask == full:
                return abs(last - nums[0])
            best = float('inf')
            for i in range(n):
                if not (mask & (1 << i)):
                    cand = abs(last - nums[i]) + dp(mask | (1 << i), i)
                    if cand < best:
                        best = cand
            return best

        minscore = dp(1 << 0, 0)  # nums problems of this type fix start at 0 (lexicographically smallest must start at 0 if optimal)

        # reconstruct lexicographically smallest optimal permutation, starting at 0
        ans1 = [0]
        used = [False] * n
        used[0] = True
        mask = 1 << 0
        last = 0
        remaining = minscore

        for _ in range(n - 1):
            for i in range(n):
                if used[i]:
                    continue
                cost_here = abs(last - nums[i])
                if cost_here + dp(mask | (1 << i), i) == remaining:
                    ans1.append(i)
                    used[i] = True
                    mask |= (1 << i)
                    remaining -= cost_here
                    last = i
                    break

        return ans1