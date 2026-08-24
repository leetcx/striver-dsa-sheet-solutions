class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[] for _ in range(n)]
        visited=[False] *n
        
        for i in range(len(edges)):
            s=edges[i][0]
            d=edges[i][1]
            adj[s].append(d)
            adj[d].append(s)
        if source==destination:
            return True        
        def dfs(node):
            nonlocal visited
            visited[node]=True
            for j in range(len(adj[node])):
                neigh=adj[node][j]
                if neigh==destination :
                    return True
                if visited[neigh]==False:
                    if dfs(neigh):
                        return True
            return False
        for k in range(n):
            if k==source:
                if dfs(source):
                    return True
        return False
                