import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        maxheap=[]
        for idx,i in enumerate(mat):
            sum1=sum(i)
            if len(maxheap)<k:
                heapq.heappush(maxheap,(-sum1,-idx))
            else:
                 if (sum1 < -maxheap[0][0]) or (sum1 == -maxheap[0][0] and idx < -maxheap[0][1]):
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap,(-sum1,-idx))
        res=[]
        while maxheap:
            res.append(-maxheap[0][1])
            heapq.heappop(maxheap)
        res.reverse()
        return res
