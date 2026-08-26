import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        q=[]
        sum1=0
        heapq.heappush(q,(0,0))

        visited=[False] * n
       
        while q:
            wt,node=heapq.heappop(q)
            
            if visited[node]:
                continue
            visited[node]=True
            sum1+=wt
            for i in range (len(points)):
                x1,y1=points[node]
                if visited[i]==False:
                    
                    x2,y2=points[i]
                    cost=abs(x1-x2) +abs(y1-y2)
                    heapq.heappush(q,(cost,i))
        return sum1
                