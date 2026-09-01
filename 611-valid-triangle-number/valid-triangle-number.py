class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for high in range(len(nums) - 1, 1, -1):
            low = 0
            mid = high - 1

            while low < mid:
                if nums[low] + nums[mid] > nums[high]:
                    count += mid - low
                    mid -= 1
                else:
                    low += 1

        return count