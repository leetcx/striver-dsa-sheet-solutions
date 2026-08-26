class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m=len(edges)
        adj=[[] for _ in range(m+1)]
        def dfs(i,j,visited,adj):
            visited[i]=True
            for k in range(len(adj[i])):
                neigh=adj[i][k]
                if neigh==j:
                    return True
                if visited[neigh]==False:
                    if dfs(neigh,j,visited,adj):
                        return True
            return False

        for i in range(m):
            visited=[False] * (m+1)
            s=edges[i][0]
            d=edges[i][1]
            if dfs(s,d,visited,adj)==True:
                return [s,d]
            adj[s].append(d)
            adj[d].append(s)