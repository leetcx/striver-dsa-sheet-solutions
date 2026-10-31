class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        from functools import lru_cache

        @lru_cache(None)
        def mini(i, k):
            if i == n:
                return 0 if k == 0 else float('inf')

            if k == 0:
                return float('inf')

            ans = float('inf')

            for j in range(i, n):
                mid = (i + j) // 2
                cost = 0

                for x in range(i, j + 1):
                    cost += abs(houses[x] - houses[mid])

                ans = min(ans, cost + mini(j + 1, k - 1))

            return ans

        return mini(0, k)