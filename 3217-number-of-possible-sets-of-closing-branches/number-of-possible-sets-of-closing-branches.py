import heapq
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        nums=[]
        for i in range(n):
            nums.append(i)
        ans=[]
        temp=[]
        def backtrack(i):
            nonlocal ans
            nonlocal temp
            if i>=n:
                ans.append(temp.copy())
                return 
            temp.append(i)
            backtrack(i+1)
            temp.pop()
            backtrack(i+1)
        backtrack(0)
        adj=[[] for _ in range(n)]
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        def dijkstra(start,active):
            distance=[float('inf')] * n
            distance[start]=0
            minheap=[]
            heapq.heappush(minheap,(0,start))
            while minheap:
                dist,node=heapq.heappop(minheap)
                if dist>distance[node]:
                    continue
                for neigh in adj[node]:
                    nody=neigh[0]
                    w=neigh[1]
                    if nody not in active:
                        continue
                    if dist+w<distance[nody]:
                        distance[nody]=dist+w
                        heapq.heappush(minheap,(dist+w,nody))
            return max(distance[node] for node in active)
        count=0
        for j in range(len(ans)):
            active=set(ans[j])
            valid=True
            for start in active:
                if dijkstra(start,active)>maxDistance:
                    valid=False
                    break
            if valid==True:
                count+=1
        return count
            
                    


        