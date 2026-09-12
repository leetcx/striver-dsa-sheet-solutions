import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n=len(heights)
        maxheap=[]
        for i in range(n-1):
            diff=heights[i+1]-heights[i]
            if diff<=0:
                continue
            heapq.heappush(maxheap,-diff)
            bricks-=diff
            if bricks<0 and ladders>0:
                ladders-=1
                largest=-heapq.heappop(maxheap)
                bricks+=largest
            elif bricks<0 and ladders<=0:
                return i
        return n-1
