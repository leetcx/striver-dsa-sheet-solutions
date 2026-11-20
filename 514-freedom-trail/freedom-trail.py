import heapq
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n=len(ring)
        adj={}
        m=len(key)
        for i in range(n):
            if ring[i] not in adj:
                adj[ring[i]]=[]
            adj[ring[i]].append(i)
        visited=set()
        minheap=[]
        heapq.heappush(minheap,(0,0,0))
       
        totalsteps=0
        def countsteps(rindex,neigh,n):
            clock=abs(neigh-rindex)
            anti=n-clock
            return min(clock,anti)
        while minheap:
            steps,rindex,kindex=heapq.heappop(minheap)
            if kindex>=len(key):
                return steps+m
            if (rindex,kindex) in visited:
                continue
            visited.add((rindex,kindex))
            for neigh in adj[key[kindex]]:
                cost=countsteps(rindex,neigh,n)
                heapq.heappush(minheap,(steps+cost,neigh,kindex+1))
                
        return -1
