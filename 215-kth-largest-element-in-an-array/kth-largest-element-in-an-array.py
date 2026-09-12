import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap=[]
        for i in range(len(nums)):
            if len(minheap) < k:
                heapq.heappush(minheap,nums[i])
            else:
                if nums[i] > minheap[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap,nums[i])
        return minheap[0] 