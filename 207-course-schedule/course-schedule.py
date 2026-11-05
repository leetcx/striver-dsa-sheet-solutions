class Solution:
    def canFinish(self, n: int, pr: list[list[int]]) -> bool:
        
        inrecur=[False] * n
        visited=[False] * n
        
        adj=[[] for _ in range(n)]
        for u,v in pr:
            adj[v].append(u)
        def iscycle(adj,node):
            visited[node]=True
            inrecur[node]=True
            for neigh in adj[node]:
                if visited[neigh]==False and iscycle(adj,neigh):
                    return True
                elif inrecur[neigh]==True:
                    return True
            inrecur[node]=False
            return False
        for i in range(len(adj)):
            if visited[i]==False and iscycle(adj,i):
                return False
        return True