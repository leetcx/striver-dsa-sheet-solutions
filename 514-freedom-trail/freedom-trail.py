class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        memo = {}

        def mini(i, j):
            if j >= len(key):
                return 0

            state = (i, j)
            if state in memo:
                return memo[state]

            result = float('inf')

            for k in range(n):
                if ring[k] == key[j]:
                    clockwise = abs(i - k)
                    anticlockwise = n - clockwise
                    steps = min(clockwise, anticlockwise)

                    result = min(result, steps + 1 + mini(k, j + 1))

            memo[state] = result
            return memo[state]

        return mini(0, 0)