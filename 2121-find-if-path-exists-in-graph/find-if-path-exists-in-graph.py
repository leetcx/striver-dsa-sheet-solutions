class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj=[[] for _ in range(n)]
        visited=[False] * n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node):
            if node==destination:
                return  True
            visited[node]=True
            for neigh in adj[node]:
                
                if visited[neigh]==False and dfs(neigh):
                    return True
            return False
        return dfs(source)
                    
                
        