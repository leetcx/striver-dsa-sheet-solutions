import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
       
        visited=[False] * n
        res=0
       
        pq=[]
        heapq.heappush(pq,(0,0))
        while pq:
            weight,node=heapq.heappop(pq)
            if visited[node]==True:
                continue
            visited[node]=True
            res=res+weight
            x1, y1 = points[node]
            for k in range(n):
               
                if visited[k]==False:
                    x2, y2 = points[k]
                    new=abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(pq,(new,k))
        return res