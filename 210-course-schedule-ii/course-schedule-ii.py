
class Solution:
    def findOrder(self, n: int, pr: list[list[int]]) -> list[int]:
        st=[]
        visited=[False] * n
        inrecur=[False] * n
        adj=[[] for _ in range(n)]
        for u,v in pr:
            adj[v].append(u)
        def dfs(adj,node):
            visited[node]=True
            inrecur[node]=True
            for neigh in adj[node]:
                if visited[neigh]==False and dfs(adj,neigh):
                    return []
                elif inrecur[neigh]==True:
                    return []
            inrecur[node]=False
            st.append(node)
        for z in range(len(adj)):
            if visited[z]==False:
                dfs(adj,z)
        if len(st)==n:
            return st[::-1]    
        else:
            return []

        
