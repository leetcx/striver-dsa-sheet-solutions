import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[]
        for i in stones:
            heapq.heappush(maxheap,-i)
        while maxheap:
            if len(maxheap)>=2:
                first = -heapq.heappop(maxheap)
                second = -heapq.heappop(maxheap)
                if first != second:
                    
                    g=first-second
                    
                    heapq.heappush(maxheap,-g)
            else:
                if len(maxheap)==1:
                    return -maxheap[0]
                else:
                    return 0


        return 0




