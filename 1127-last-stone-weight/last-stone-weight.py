import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[]
        for i in stones:
            heapq.heappush(maxheap,-i)
        while  len(maxheap)>1:
            x=-heapq.heappop(maxheap)
            if maxheap:
                y=-heapq.heappop(maxheap)
                if x!=y:
                    heapq.heappush(maxheap,-(x-y))
        
        return -maxheap[0] if maxheap else 0

