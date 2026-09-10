import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxheap=[]
        for i in arr:
            dist=abs(i-x)
            if len(maxheap) < k:
                heapq.heappush(maxheap,(-dist,i))
            else:
                if dist<-maxheap[0][0]:
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap,(-dist,i))
        res=[]
        while maxheap:
            res.append(maxheap[0][1])
            heapq.heappop(maxheap)
        res.sort()
        return res

