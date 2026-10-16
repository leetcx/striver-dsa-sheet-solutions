import heapq
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        heap = []
        maxsum = float('-inf')

        for i in range(n):
            while heap and heap[0][1] < i - k:
                heapq.heappop(heap)

            dp[i] = nums[i]

            if heap and -heap[0][0] > 0:
                dp[i] = max(dp[i], nums[i] - heap[0][0])

            maxsum = max(maxsum, dp[i])
            heapq.heappush(heap, (-dp[i], i))

        return maxsum