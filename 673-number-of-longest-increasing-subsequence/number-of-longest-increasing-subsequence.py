class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        set1 = {i: 1 for i in range(n)}
        ways = {i: 1 for i in range(n)}

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    z = set1[j] + 1

                    if z > set1[i]:
                        set1[i] = z
                        ways[i] = ways[j]

                    elif z == set1[i]:
                        ways[i] += ways[j]

        longest = max(set1.values())
        res = 0

        for i in range(n):
            if set1[i] == longest:
                res += ways[i]

        return res