import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(i):
            k=i[0] * i[0] + i[1] * i[1]
            return k
        maxheap=[]
        for i in points:
            p=dist(i)
            if len(maxheap)<k:
                heapq.heappush(maxheap,(-p,i))
            else:
                t,idx=heapq.heappop(maxheap)
                if p< -t:
                    heapq.heappush(maxheap,(-p,i))
                else:
                    heapq.heappush(maxheap,(t,idx))

        res=[]
        while maxheap:
            i,j=heapq.heappop(maxheap)
            res.append(j)
        return res
