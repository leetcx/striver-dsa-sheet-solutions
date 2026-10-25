from functools import lru_cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def maxi(i, mask, allowed):
            if i == n:
                return 1

            ans = 0

            bit = 1 << (ord(s[i]) - ord('a'))
            newmask = mask | bit

            if newmask.bit_count() <= k:
                ans = max(ans, maxi(i + 1, newmask, allowed))
            else:
                ans = max(ans, 1 + maxi(i + 1, bit, allowed))

            if allowed:
                for ch in range(26):
                    bit = 1 << ch
                    newmask = mask | bit

                    if newmask.bit_count() <= k:
                        ans = max(ans, maxi(i + 1, newmask, 0))
                    else:
                        ans = max(ans, 1 + maxi(i + 1, bit, 0))

            return ans

        return maxi(0, 0, 1)
        