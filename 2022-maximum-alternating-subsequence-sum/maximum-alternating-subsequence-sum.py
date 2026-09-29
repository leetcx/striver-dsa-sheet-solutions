class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        even = 0
        odd = 0

        for x in nums:
            new_even = max(even, odd + x)
            new_odd = max(odd, even - x)

            even = new_even
            odd = new_odd

        return even