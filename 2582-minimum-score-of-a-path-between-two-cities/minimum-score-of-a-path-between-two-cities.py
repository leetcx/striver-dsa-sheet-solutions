

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        adj = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        visited=[False] * (n+1)
        result=float('inf')
        def dfs(node,adj,visited):
            nonlocal result
            visited[node]=True
            
            for neigh in adj[node]:
                nody=neigh[0]
                wt=neigh[1]
                result=min(result,wt)
                if visited[nody]==False:
                   
                    dfs(nody,adj,visited)
        dfs(1,adj,visited)
        return result