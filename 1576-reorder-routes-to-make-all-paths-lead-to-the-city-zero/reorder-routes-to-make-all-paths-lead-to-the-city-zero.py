class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in connections:
            adj[u].append((v,1))
            adj[v].append((u,0))
        ans=0
        visited=[False] *  n
        def dfs(node,adj,visited):
            nonlocal ans
            visited[node]=True
            for neigh,cost in adj[node]:
                if visited[neigh]==False:
                    ans+=cost
                    dfs(neigh,adj,visited)
        dfs(0,adj,visited)
        return ans