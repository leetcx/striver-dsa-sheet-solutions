import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxheap=[]
        for i in range(len(piles)):
            heapq.heappush(maxheap,(-piles[i],i))
        while k:
            if maxheap:
                t,idx=heapq.heappop(maxheap)
                d=floor((-t)/2)
                diff=(-t)-d
                heapq.heappush(maxheap,(-diff,idx))
            k-=1
        sum1=0
        while maxheap:
            z,indi=heapq.heappop(maxheap)
            sum1+=(-z)
        return sum1

