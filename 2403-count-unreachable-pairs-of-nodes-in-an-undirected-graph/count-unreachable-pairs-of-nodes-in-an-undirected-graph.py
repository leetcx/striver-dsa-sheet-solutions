class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*n
        ans=0
        remaining=n
        def dfs(node,adj):
            nonlocal count
            visited[node]=True
            count+=1
            for neigh in adj[node]:
                if visited[neigh]==False:
                   
                    dfs(neigh,adj)
            
        for i in range(n):
            if visited[i]==False:
                count=0
                dfs(i,adj)
                remaining -= count
                ans+=count*remaining
        return ans

        