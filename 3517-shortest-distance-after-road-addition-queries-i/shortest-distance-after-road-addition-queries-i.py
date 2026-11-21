import heapq
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(n)]
        for i in range(n-1):
            adj[i].append((i+1,1))       
        def bfs(adj):
            minheap=[]
            heapq.heappush(minheap,(0,0))
            distance=[float('inf')]*n
            distance[0]=0
            while minheap:
                dist,node=heapq.heappop(minheap)
                if dist>distance[node]:
                    continue
                for neigh in adj[node]:
                    nody=neigh[0]
                    wt=neigh[1]
                    if dist+wt<distance[nody]:
                        distance[nody]=dist+wt
                        heapq.heappush(minheap,(dist+wt,nody))
            return distance[n-1]
        ans=[]
        for u,v in queries:
            adj[u].append((v,1))
            z=bfs(adj)
            ans.append(z)
        return ans
