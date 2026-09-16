import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minheap=[]
        for i in range(k):
            heapq.heappush(minheap,nums[i])
        for i in range(k,len(nums)):
            if minheap and minheap[0] < nums[i]:
                heapq.heappop(minheap)
                heapq.heappush(minheap,nums[i])
        return minheap[0]
        