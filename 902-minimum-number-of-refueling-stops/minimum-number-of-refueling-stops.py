class Solution:
    def minRefuelStops(self, target: int, startfuel: int, stations: List[List[int]]) -> int:
        stations.sort()
        idx=0
        minheap=[]
        n=len(stations)
        c=0
        while startfuel < target:
            while idx < n and  startfuel >= stations[idx][0]:
                
                heapq.heappush(minheap,-stations[idx][1])
                idx+=1
            if not minheap:
                return -1
            d=-heapq.heappop(minheap)
            startfuel+=d
            c+=1
            
        return c
           
                
            

            

