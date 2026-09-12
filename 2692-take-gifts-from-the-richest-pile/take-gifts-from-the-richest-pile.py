import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap=[]
        for i in range(len(gifts)):
            heapq.heappush(maxheap,-gifts[i])
        while k>0:
            if maxheap:
                t=-heapq.heappop(maxheap)
                x=int(math.sqrt(t))
                heapq.heappush(maxheap,-x)
            k-=1
        sum1=0
        while maxheap:
            d=-heapq.heappop(maxheap)
            sum1+=d
        return sum1

