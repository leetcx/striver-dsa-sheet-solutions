import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        adj=[[] for _ in range(len(points))]

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist=abs(points[i][0]-points[j][0])+ abs(points[i][1]-points[j][1])
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        minheap=[]
        visited=[False] * len(points)
        sum1=0
        heapq.heappush(minheap,(0,0))
        while minheap:
            wt,node=heapq.heappop(minheap)
            if visited[node]==True:
                continue
            visited[node]=True
            sum1+=wt
            for neigh in adj[node]:
                dist=neigh[0]
                nom=neigh[1]
                if visited[nom]==False:
                    heapq.heappush(minheap,(dist,nom))
        return sum1


        