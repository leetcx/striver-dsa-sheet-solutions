import heapq
class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:

        adj=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w)) 
            adj[v].append((u,w))
        def bfs(node):
            minheap=[]
            heapq.heappush(minheap,(0,node))
            distance=[float('inf')] * n
            distance[node]=0
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
            return distance   
        dist1=bfs(0)
        dist2=bfs(n-1)
        if dist1[n-1]==float('inf'):
            return [False]* len(edges)
        ans=[]
        for u,v,w in edges:
            main1=dist1[u]+w+dist2[v]
            main2=dist1[v]+w+dist2[u]
            if main1==dist1[n-1] or main2==dist1[n-1]:
                ans.append(True)
            else:
                ans.append(False)
        return ans