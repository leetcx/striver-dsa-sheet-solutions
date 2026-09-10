import math


import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(i):
            k=i[0]*i[0] + i[1]*i[1]
            decu=math.sqrt(k)
            return decu
        maxheap=[]
        for i in points:
            t=dist(i)
            if len(maxheap)<k:
                heapq.heappush(maxheap,(-t,i))
            else:
                if t<-maxheap[0][0]:
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap,(-t,i))
        res=[]
        while maxheap:
            res.append(maxheap[0][1])
            heapq.heappop(maxheap)
        return res
