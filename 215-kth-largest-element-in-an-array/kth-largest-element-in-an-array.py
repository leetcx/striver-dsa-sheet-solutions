import heapq
class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        maxheap=[]
        for i in range(len(arr)):
            if len(maxheap)<k:
                heapq.heappush(maxheap,arr[i])
            else:
                if arr[i] > maxheap[0]:
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap,arr[i])
        return maxheap[0]    