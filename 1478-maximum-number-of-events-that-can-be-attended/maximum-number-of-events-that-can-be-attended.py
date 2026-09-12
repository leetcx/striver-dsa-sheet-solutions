import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        minheap=[]
        events.sort()
        d=0
        idx=0
        res=0
        for i in range(len(events)):
            if not minheap:
                d=max(events[i][0],d) 
            while idx<len(events) and d>=events[idx][0]:
                heapq.heappush(minheap,events[idx][1])  
                idx+=1
            while minheap and d>minheap[0]:
                heapq.heappop(minheap)
            if minheap:
                end=heapq.heappop(minheap)
                d+=1
                res+=1
        return res