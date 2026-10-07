class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort(reverse=True)

        total = 0
        ans = 0

        for x in satisfaction:
            total += x

            if total > 0:
                ans += total
            else:
                break

        return ans
            